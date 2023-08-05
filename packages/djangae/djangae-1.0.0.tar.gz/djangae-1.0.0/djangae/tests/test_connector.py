# encoding: utf-8

import datetime
import decimal
import logging
import random
import re
import uuid
from hashlib import md5
from io import StringIO
from string import letters
from unittest import skipIf

# LIBRARIES
import django
from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import FieldError, ValidationError
from django.core.files.uploadhandler import StopFutureHandlers
from django.db import DataError, IntegrityError, NotSupportedError
from django.db import connection as default_connection
from django.db import models
from django.db.models.query import Q
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.template import Context, Template
from django.test import RequestFactory
from django.test.utils import override_settings
from django.utils import six
from django.utils.safestring import SafeText
from django.utils.six.moves import range
from google.appengine.api import taskqueue
from google.appengine.api.datastore_errors import (EntityNotFoundError,
                                                   TransactionFailedError)
from google.appengine.datastore import datastore_rpc
from google.appengine.ext import deferred

# DJANGAE
from djangae.contrib import sleuth
from djangae.core import paginator
from djangae.db import constraints
from djangae.db.backends.appengine import indexing, rpc
from djangae.db.backends.appengine.commands import FlushCommand
from djangae.db.backends.appengine.indexing import (IExactIndexer,
                                                    add_special_index,
                                                    get_indexer)
from djangae.db.caching import disable_cache
from djangae.db.constraints import UniqueMarker, UniquenessMixin
from djangae.db.unique_utils import (_unique_combinations,
                                     unique_identifiers_from_entity)
from djangae.db.utils import (decimal_to_string, entity_matches_query,
                              normalise_field_value)
from djangae.fields import CharField, ListField, RelatedSetField, SetField
from djangae.storage import BlobstoreFileUploadHandler
from djangae.test import TestCase, inconsistent_db

DEFAULT_NAMESPACE = default_connection.ops.connection.settings_dict.get("NAMESPACE")


try:
    import webtest
except ImportError:
    webtest = NotImplemented


class TestUser(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    last_login = models.DateField(auto_now_add=True)
    field2 = models.CharField(max_length=32)

    def __unicode__(self):
        return self.username

    class Meta:
        app_label = "djangae"


class ModelWithNullableCharField(models.Model):
    field1 = models.CharField(max_length=500, null=True)
    some_id = models.IntegerField(default=0)

    class Meta:
        app_label = "djangae"


class UniqueModel(models.Model):
    unique_field = models.CharField(max_length=100, unique=True)
    unique_combo_one = models.IntegerField(blank=True, default=0)
    unique_combo_two = models.CharField(max_length=100, blank=True, default="")

    unique_relation = models.ForeignKey('self', null=True, blank=True, unique=True)

    unique_set_field = SetField(models.CharField(max_length=500), unique=True)
    unique_list_field = ListField(models.CharField(max_length=500), unique=True)

    unique_together_list_field = ListField(models.IntegerField())

    class Meta:
        unique_together = [
            ("unique_combo_one", "unique_combo_two"),
            ("unique_together_list_field", "unique_combo_one")
        ]

        app_label = "djangae"


class UniqueModelWithLongPK(models.Model):
    long_pk = models.CharField(max_length=500, primary_key=True)
    unique_field = models.IntegerField(unique=True)


class IntegerModel(models.Model):
    integer_field = models.IntegerField()

    class Meta:
        app_label = "djangae"


class TestFruit(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    origin = models.CharField(max_length=32, default="Unknown")
    color = models.CharField(max_length=100)
    is_mouldy = models.BooleanField(default=False)
    text_field = models.TextField(blank=True, default="")
    binary_field = models.BinaryField(blank=True)

    class Meta:
        ordering = ("color",)
        app_label = "djangae"

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return "<TestFruit: name={}, color={}>".format(self.name, self.color)


class Permission(models.Model):
    user = models.ForeignKey(TestUser)
    perm = models.CharField(max_length=32)

    def __unicode__(self):
        return u"{0} for {1}".format(self.perm, self.user)

    class Meta:
        ordering = ('user__username', 'perm')
        app_label = "djangae"


class SelfRelatedModel(models.Model):
    related = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        app_label = "djangae"


class MultiTableParent(models.Model):
    parent_field = models.CharField(max_length=32)

    class Meta:
        app_label = "djangae"


class MultiTableChildOne(MultiTableParent):
    child_one_field = models.CharField(max_length=32)

    class Meta:
        app_label = "djangae"


class MultiTableChildTwo(MultiTableParent):
    child_two_field = models.CharField(max_length=32)

    class Meta:
        app_label = "djangae"


class Relation(models.Model):
    class Meta:
        app_label = "djangae"


class Related(models.Model):
    headline = models.CharField(max_length=500)
    relation = models.ForeignKey(Relation)

    class Meta:
        app_label = "djangae"


class NullDate(models.Model):
    date = models.DateField(null=True, default=None)
    datetime = models.DateTimeField(null=True, default=None)
    time = models.TimeField(null=True, default=None)

    class Meta:
        app_label = "djangae"


class NullDateSet(models.Model):
    dates = RelatedSetField(NullDate, blank=True, unique=True)

    class Meta:
        app_label = "djangae"


class ModelWithUniques(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        app_label = "djangae"


class ModelWithUniquesOnForeignKey(models.Model):
    name = models.CharField(max_length=64, unique=True)
    related_name = models.ForeignKey(ModelWithUniques, unique=True)

    class Meta:
        unique_together = [("name", "related_name")]
        app_label = "djangae"


class ModelWithDates(models.Model):
    start = models.DateField()
    end = models.DateField()

    class Meta:
        app_label = "djangae"


class ModelWithUniquesAndOverride(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Djangae:
        disable_constraint_checks = False

    class Meta:
        app_label = "djangae"


class SpecialIndexesModel(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    nickname = CharField(blank=True)
    sample_list = ListField(models.CharField)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "djangae"


class DateTimeModel(models.Model):
    datetime_field = models.DateTimeField(auto_now_add=True)
    date_field = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "djangae"


if django.VERSION >= (1, 8):
    # DurationField was only introducd in Django 1.8

    class DurationModel(models.Model):

        duration_field = models.DurationField()
        duration_field_nullable = models.DurationField(blank=True, null=True)


class PaginatorModel(models.Model):
    foo = models.IntegerField()

    class Meta:
        app_label = "djangae"


class BackendTests(TestCase):
    def test_pk_gt_empty_returns_all(self):
        for i in range(10):
            TestFruit.objects.create(name=str(i), color=str(i))

        self.assertEqual(10, TestFruit.objects.filter(pk__gt="").count())
        self.assertEqual(10, TestFruit.objects.filter(pk__gte="").count())
        self.assertEqual(0, TestFruit.objects.filter(pk__lt="").count())
        self.assertEqual(0, TestFruit.objects.filter(pk__lte="").count())

    def test_pk_gt_zero_returns_all(self):
        IntegerModel.objects.create(pk=1, integer_field=1)
        IntegerModel.objects.create(pk=2, integer_field=2)

        results = IntegerModel.objects.filter(pk__gt=0)
        self.assertEqual(2, len(results))

        results = IntegerModel.objects.filter(pk__gte=0)
        self.assertEqual(2, len(results))

        results = IntegerModel.objects.filter(pk__lt=0)
        self.assertEqual(0, len(results))

        results = IntegerModel.objects.filter(pk__lte=0)
        self.assertEqual(0, len(results))

    def test_entity_matches_query(self):
        entity = rpc.Entity("test_model")
        entity["name"] = "Charlie"
        entity["age"] = 22

        query = rpc.Query("test_model")
        query["name ="] = "Charlie"
        self.assertTrue(entity_matches_query(entity, query))

        query["age >="] = 5
        self.assertTrue(entity_matches_query(entity, query))
        del query["age >="]

        query["age <"] = 22
        self.assertFalse(entity_matches_query(entity, query))
        del query["age <"]

        query["age <="] = 22
        self.assertTrue(entity_matches_query(entity, query))
        del query["age <="]

        query["name ="] = "Fred"
        self.assertFalse(entity_matches_query(entity, query))

        # If the entity has a list field, then if any of them match the
        # query then it's a match
        entity["name"] = ["Bob", "Fred", "Dave"]
        self.assertTrue(entity_matches_query(entity, query))  # ListField test

    def test_exclude_pks_with_slice(self):
        for i in range(10):
            TestFruit.objects.create(name=str(i), color=str(i))

        to_exclude = [str(x) for x in list(range(5)) + list(range(15, 20))]

        to_return = TestFruit.objects.exclude(pk__in=set(to_exclude)).values_list("pk", flat=True)[:2]
        self.assertEqual(2, len(to_return))

        qs = TestFruit.objects.filter(
            pk__in=to_return
        )

        self.assertEqual(2, len(qs))

    def test_count_on_excluded_pks(self):
        TestFruit.objects.create(name="Apple", color="Red")
        TestFruit.objects.create(name="Orange", color="Orange")

        self.assertEqual(1, TestFruit.objects.filter(pk__in=["Apple", "Orange"]).exclude(pk__in=["Apple"]).count())

    def test_defaults(self):
        fruit = TestFruit.objects.create(name="Apple", color="Red")
        self.assertEqual("Unknown", fruit.origin)

        instance = rpc.Get(rpc.Key.from_path(TestFruit._meta.db_table, fruit.pk, namespace=DEFAULT_NAMESPACE))
        del instance["origin"]
        rpc.Put(instance)

        fruit = TestFruit.objects.get()
        self.assertIsNone(fruit.origin)
        fruit.save()

        fruit = TestFruit.objects.get()
        self.assertEqual("Unknown", fruit.origin)

    @disable_cache()
    def test_get_by_keys(self):
        colors = ["Red", "Green", "Blue", "Yellow", "Orange"]
        fruits = [TestFruit.objects.create(name=str(x), color=random.choice(colors)) for x in range(32)]

        # Check that projections work with key lookups
        with sleuth.watch('djangae.db.backends.appengine.rpc.Query.__init__') as query_init:
            with sleuth.watch('djangae.db.backends.appengine.rpc.Query.Ancestor') as query_anc:
                TestFruit.objects.only("color").get(pk="0").color
                self.assertEqual(query_init.calls[0].kwargs["projection"], ["color"])

                # Make sure the query is an ancestor of the key
                self.assertEqual(
                    query_anc.calls[0].args[1],
                    rpc.Key.from_path(
                        TestFruit._meta.db_table, "0", namespace=DEFAULT_NAMESPACE
                    )
                )

        # Now check projections work with fewer than 100 things
        with sleuth.watch('djangae.db.backends.appengine.meta_queries.AsyncMultiQuery.__init__') as query_init:
            with sleuth.watch('djangae.db.backends.appengine.rpc.Query.Ancestor') as query_anc:
                keys = [str(x) for x in range(32)]
                results = list(TestFruit.objects.only("color").filter(pk__in=keys).order_by("name"))

                self.assertEqual(query_init.call_count, 1) # One multiquery
                self.assertEqual(query_anc.call_count, 32) # 32 Ancestor calls
                self.assertEqual(len(query_init.calls[0].args[1]), 32)

                # Confirm the ordering is correct
                self.assertEqual(sorted(keys), [x.pk for x in results])

        results = list(TestFruit.objects.only("color").filter(pk__in=keys).order_by("name")[5:10])
        self.assertEqual(len(results), 5)
        self.assertEqual([x.pk for x in results], sorted(keys)[5:10])

        # Make sure we can do a normal (non-projection) get by keys
        self.assertItemsEqual(TestFruit.objects.filter(pk__in=keys), fruits)

    def test_get_or_create(self):
        """
            Django's get_or_create can do the following:

            1. get(**lookup) -> throws DoesNotExist
            2. Catches DoesNotExist
            3. create() -> throws IntegrityError
            4. get(**lookup)

            This test proves that we throw the right kind of error at step 3 when
            unique constraints are violated.
        """

        def wrap_get(func):
            def _wrapped(*args, **kwargs):
                try:
                    if _wrapped.calls == 0:
                        raise UniqueModel.DoesNotExist()
                    else:
                        return func(*args, **kwargs)
                finally:
                    _wrapped.calls += 1

            _wrapped.calls = 0
            return _wrapped

        from django.db.models import query
        wrapped_get = wrap_get(query.QuerySet.get)

        UniqueModel.objects.create(unique_field="Test")

        with disable_cache():
            with sleuth.switch("django.db.models.query.QuerySet.get", wrapped_get):
                instance, created = UniqueModel.objects.get_or_create(unique_field="Test")
                self.assertFalse(created)

    def test_setting_non_null_null_throws_integrity_error(self):
        with self.assertRaises(IntegrityError):
            IntegerModel.objects.create(integer_field=None)

        with self.assertRaises(IntegrityError):
            instance = IntegerModel()
            instance.integer_field = None
            instance.save()

        with self.assertRaises(IntegrityError):
            instance = IntegerModel.objects.create(integer_field=1)
            instance = IntegerModel.objects.get()
            instance.integer_field = None
            instance.save()

    def test_normalise_field_value(self):
        self.assertEqual(u'0000475231073257', normalise_field_value(decimal.Decimal(475231073257)))
        self.assertEqual(u'-0000475231073257', normalise_field_value(decimal.Decimal(-475231073257)))
        self.assertEqual(u'0000000004752311', normalise_field_value(decimal.Decimal(4752310.73257)))
        self.assertEqual(u'0000004752310733', normalise_field_value(decimal.Decimal(4752310732.57)))
        self.assertEqual(
            datetime.datetime(2015, 1, 27, 2, 46, 8, 584258),
            normalise_field_value(datetime.datetime(2015, 1, 27, 2, 46, 8, 584258))
        )

    def test_decimal_to_string(self):
        self.assertEqual(u'0002312487812767', decimal_to_string(decimal.Decimal(2312487812767)))
        self.assertEqual(u'-0002312487812767', decimal_to_string(decimal.Decimal(-2312487812767)))
        self.assertEqual(u'002312487812', decimal_to_string(decimal.Decimal(2312487812), 12))
        self.assertEqual(u'002387812.320', decimal_to_string(decimal.Decimal(2387812.32), 12, 3))
        self.assertEqual(u'-002387812.513', decimal_to_string(decimal.Decimal(-2387812.513212), 12, 3))
        self.assertEqual(u'0237812.000', decimal_to_string(decimal.Decimal(237812), 10, 3))
        self.assertEqual(u'-0237812.210', decimal_to_string(decimal.Decimal(-237812.21), 10, 3))

    def test_gae_conversion(self):
        # A PK IN query should result in a single get by key

        with sleuth.switch("djangae.db.backends.appengine.commands.rpc.Get", lambda *args, **kwargs: []) as get_mock:
            list(TestUser.objects.filter(pk__in=[1, 2, 3]))  # Force the query to run
            self.assertEqual(1, get_mock.call_count)

        with sleuth.switch(
            "djangae.db.backends.appengine.commands.rpc.Query.Run", lambda *args, **kwargs: []
        ) as query_mock:
            list(TestUser.objects.filter(username="test"))
            self.assertEqual(1, query_mock.call_count)

        with sleuth.switch(
            "djangae.db.backends.appengine.meta_queries.AsyncMultiQuery.Run", lambda *args, **kwargs: []
        ) as query_mock:
            list(TestUser.objects.filter(username__in=["test", "cheese"]))
            self.assertEqual(1, query_mock.call_count)

        with sleuth.switch(
            "djangae.db.backends.appengine.commands.rpc.Get", lambda *args, **kwargs: []
        ) as get_mock:
            list(TestUser.objects.filter(pk=1))
            self.assertEqual(1, get_mock.call_count)

        with sleuth.switch(
            "djangae.db.backends.appengine.meta_queries.AsyncMultiQuery.Run", lambda *args, **kwargs: []
        ) as query_mock:
            list(TestUser.objects.exclude(username__startswith="test"))
            self.assertEqual(1, query_mock.call_count)

        with sleuth.switch(
            "djangae.db.backends.appengine.commands.rpc.Get", lambda *args, **kwargs: []
        ) as get_mock:
            list(
                TestUser.objects.filter(pk__in=[1, 2, 3, 4, 5, 6, 7, 8]).
                filter(username__in=["test", "test2", "test3"]).
                filter(email__in=["test@example.com", "test2@example.com"])
            )

            self.assertEqual(1, get_mock.call_count)

    def test_gae_query_display(self):
        # Shouldn't raise any exceptions:
        representation = six.text_type(TestUser.objects.filter(username='test').query)
        self.assertTrue('test' in representation)
        self.assertTrue('username' in representation)

    def test_range_behaviour(self):
        IntegerModel.objects.create(integer_field=5)
        IntegerModel.objects.create(integer_field=10)
        IntegerModel.objects.create(integer_field=15)

        self.assertItemsEqual(
            [10],
            IntegerModel.objects.filter(
                integer_field__range=(6, 14)
            ).values_list("integer_field", flat=True)
        )

        self.assertItemsEqual(
            [5, 10, 15],
            IntegerModel.objects.filter(
                integer_field__range=(5, 15)
            ).order_by("integer_field").values_list("integer_field", flat=True)
        )

        self.assertItemsEqual(
            [5, 15],
            IntegerModel.objects.exclude(
                integer_field__range=(6, 14)
            ).values_list("integer_field", flat=True)
        )

    def test_exclude_nullable_field(self):
        instance = ModelWithNullableCharField.objects.create(some_id=999) # Create a nullable thing
        ModelWithNullableCharField.objects.create(some_id=999, field1="test") # Create a nullable thing
        self.assertItemsEqual(
            [instance],
            ModelWithNullableCharField.objects.filter(
                some_id=999
            ).exclude(field1="test").all()
        )

        instance.field1 = "bananas"
        instance.save()

        self.assertEqual(instance, ModelWithNullableCharField.objects.filter(some_id=999).exclude(field1="test")[0])

    def test_null_date_field(self):
        null_date = NullDate()
        null_date.save()

        null_date = NullDate.objects.get()
        self.assertIsNone(null_date.date)
        self.assertIsNone(null_date.time)
        self.assertIsNone(null_date.datetime)

    def test_convert_unicode_subclasses_to_unicode(self):
        # The App Engine SDK raises BadValueError if you try saving a SafeText
        # string to a CharField. Djangae explicitly converts it to unicode.
        grue = SafeText(u'grue')

        self.assertIsInstance(grue, unicode)
        self.assertNotEqual(type(grue), unicode)

        obj = TestFruit.objects.create(name=u'foo', color=grue)
        obj = TestFruit.objects.get(pk=obj.pk)
        self.assertEqual(type(obj.color), unicode)

        obj = TestFruit.objects.filter(color=grue)[0]
        self.assertEqual(type(obj.color), unicode)

    def test_notsupportederror_thrown_on_too_many_inequalities(self):
        TestFruit.objects.create(name="Apple", color="Green", origin="England")
        pear = TestFruit.objects.create(name="Pear", color="Green")
        banana = TestFruit.objects.create(name="Banana", color="Yellow")

        # Excluding one field is fine
        self.assertItemsEqual([pear, banana], list(TestFruit.objects.exclude(name="Apple")))

        # Excluding a field, and doing a > or < on another is not so fine
        with self.assertRaises(NotSupportedError):
            self.assertEqual(pear, TestFruit.objects.exclude(origin="England").filter(color__lt="Yellow").get())

        # Same with excluding two fields
        with self.assertRaises(NotSupportedError):
            list(TestFruit.objects.exclude(origin="England").exclude(color="Yellow"))

        # But apparently excluding the same field twice is OK
        self.assertItemsEqual(
            [banana],
            list(TestFruit.objects.exclude(
                origin="England"
            ).exclude(name="Pear").order_by("origin"))
        )

        # And apparently having both a __gt and a __lt filter on the same field is also fine
        self.assertItemsEqual([banana], list(TestFruit.objects.order_by().filter(name__lt="Pear", name__gt="Apple")))

    def test_excluding_pks_is_emulated(self):
        apple = TestFruit.objects.create(name="Apple", color="Green", is_mouldy=True, origin="England")
        banana = TestFruit.objects.create(name="Banana", color="Yellow", is_mouldy=True, origin="Dominican Republic")
        cherry = TestFruit.objects.create(name="Cherry", color="Red", is_mouldy=True, origin="Germany")
        pear = TestFruit.objects.create(name="Pear", color="Green", origin="England")

        self.assertEqual(
            [apple, pear],
            list(TestFruit.objects.filter(origin__lt="Germany").exclude(
                pk=banana.pk
            ).exclude(pk=cherry.pk).order_by("origin"))
        )

        self.assertEqual(
            [apple, cherry],
            list(TestFruit.objects.exclude(
                origin="Dominican Republic"
            ).exclude(pk=pear.pk).order_by("origin"))
        )

        self.assertEqual(
            [],
            list(TestFruit.objects.filter(
                is_mouldy=True
            ).filter(
                color="Green", origin__gt="England"
            ).exclude(pk=pear.pk).order_by("-origin"))
        )

        self.assertEqual([cherry, banana], list(TestFruit.objects.exclude(pk=pear.pk).order_by("-name")[:2]))
        self.assertEqual([banana, apple], list(TestFruit.objects.exclude(pk=pear.pk).order_by("origin", "name")[:2]))

    def test_datetime_fields(self):
        date = datetime.datetime.today()
        dt = datetime.datetime.now()
        time = datetime.time(0, 0, 0)

        # check if creating objects work
        obj = NullDate.objects.create(date=date, datetime=dt, time=time)

        # check if filtering objects work
        self.assertItemsEqual([obj], NullDate.objects.filter(datetime=dt))
        self.assertItemsEqual([obj], NullDate.objects.filter(date=date))
        self.assertItemsEqual([obj], NullDate.objects.filter(time=time))

        # check if updating objects work
        obj.date = date + datetime.timedelta(days=1)
        obj.datetime = dt + datetime.timedelta(days=1)
        obj.time = datetime.time(23, 0, 0)
        obj.save()
        self.assertItemsEqual([obj], NullDate.objects.filter(datetime=obj.datetime))
        self.assertItemsEqual([obj], NullDate.objects.filter(date=obj.date))
        self.assertItemsEqual([obj], NullDate.objects.filter(time=obj.time))

    def test_related_datetime_nullable(self):
        date = datetime.datetime.today()
        dt = datetime.datetime.now()
        time = datetime.time(0, 0, 0)

        date_set = NullDateSet.objects.create()
        empty_obj = NullDate.objects.create(date=None, datetime=None, time=None)
        date_set.dates.add(empty_obj)

        obj = NullDate.objects.create(date=date, datetime=dt, time=time)
        date_set.dates.add(obj)
        date_set.save()

        # check if filtering/excluding of None works in RelatedSetField
        self.assertItemsEqual([obj], date_set.dates.filter(datetime__isnull=False))
        self.assertItemsEqual([obj], date_set.dates.filter(date__isnull=False))
        self.assertItemsEqual([obj], date_set.dates.filter(time__isnull=False))

        self.assertItemsEqual([obj], date_set.dates.exclude(datetime=None))
        self.assertItemsEqual([obj], date_set.dates.exclude(date=None))
        self.assertItemsEqual([obj], date_set.dates.exclude(time=None))

        # sorting should work too
        self.assertItemsEqual([obj, empty_obj], date_set.dates.order_by('datetime'))
        self.assertItemsEqual([empty_obj, obj], date_set.dates.order_by('-datetime'))
        self.assertItemsEqual([obj, empty_obj], date_set.dates.order_by('date'))
        self.assertItemsEqual([empty_obj, obj], date_set.dates.order_by('-date'))
        self.assertItemsEqual([obj, empty_obj], date_set.dates.order_by('time'))
        self.assertItemsEqual([empty_obj, obj], date_set.dates.order_by('-time'))

    def test_update_with_f_expr(self):
        i = IntegerModel.objects.create(integer_field=1000)
        qs = IntegerModel.objects.all()
        qs.update(integer_field=models.F('integer_field') + 1)

        self.assertRaises(IntegerModel.DoesNotExist, IntegerModel.objects.get, integer_field=1000)
        i = IntegerModel.objects.get(pk=i.pk)
        self.assertEqual(1001, i.integer_field)

    def test_save_with_f_expr(self):
        i = IntegerModel.objects.create(integer_field=1000)

        i.integer_field = models.F('integer_field') + 1
        i.save()

        self.assertRaises(IntegerModel.DoesNotExist, IntegerModel.objects.get, integer_field=1000)
        i = IntegerModel.objects.get(pk=i.pk)
        self.assertEqual(1001, i.integer_field)

    def test_ordering_by_scatter_property(self):
        try:
            list(TestFruit.objects.order_by("__scatter__"))
        except:  # noqa
            logging.exception("Error sorting on __scatter__")
            self.fail("Unable to sort on __scatter__ property like we should")

    def test_ordering_on_non_indexed_fields_not_supported(self):
        self.assertRaises(NotSupportedError, list, TestFruit.objects.order_by("text_field"))
        self.assertRaises(NotSupportedError, list, TestFruit.objects.order_by("binary_field"))

    def test_ordering_on_sparse_field(self):
        """
        Case when sorting on field that is not present in all of
        Datastore entities. That can easily happen when you added
        new field to model and did not populated all existing entities
        """
        # Clean state
        self.assertEqual(TestFruit.objects.count(), 0)

        # Put constistent instances to Datastore
        TestFruit.objects.create(name='a', color='a')
        TestFruit.objects.create(name='b', color='b')

        # Put inconsistent instances to Datastore
        # Color fields is missing (not even None)
        # we need more than 1 so we explore all sorting branches
        values = {'name': 'c'}
        entity = rpc.Entity(TestFruit._meta.db_table, namespace=DEFAULT_NAMESPACE, **values)
        entity.update(values)
        rpc.Put(entity)

        values = {'name': 'd'}
        entity = rpc.Entity(TestFruit._meta.db_table, namespace=DEFAULT_NAMESPACE, **values)
        entity.update(values)
        rpc.Put(entity)

        # Ok, we can get all 4 instances
        self.assertEqual(TestFruit.objects.count(), 4)

        # Sorted list. No exception should be raised
        # (esp KeyError from django_ordering_comparison)
        with sleuth.watch('djangae.db.backends.appengine.commands.utils.django_ordering_comparison') as compare:
            all_names = ['a', 'b', 'c', 'd']
            fruits = list(
                TestFruit.objects.filter(name__in=all_names).order_by('color', 'name')
            )
            # Make sure troubled code got triggered
            # ie. with all() it doesn't
            self.assertTrue(compare.called)

        # Test the ordering of the results.  The ones with a color of None should come back first,
        # and of the ones with color=None, they should be ordered by name
        # Missing one (None) as first
        expected_fruits = [
            ('c', None), ('d', None), ('a', 'a'), ('b', 'b'),
        ]

        self.assertEqual(
            [(fruit.name, fruit.color) for fruit in fruits],
            expected_fruits,
        )

    def test_update_query_does_not_update_entities_which_no_longer_match_query(self):
        """ When doing queryset.update(field=x), any entities which the query returns but which no
            longer match the query (due to eventual consistency) should not be altered.
        """
        obj = TestFruit.objects.create(name='apple', color='green', is_mouldy=False)
        with inconsistent_db(probability=0):
            # alter our object, so that it should no longer match the query that we then do
            obj.color = 'blue'
            obj.save()
            # Now run a query, our object is changed, but the inconsistency means it will still match
            queryset = TestFruit.objects.filter(color='green')
            assert queryset.count(), "inconsistent_db context manager isn't working" # sanity
            # Now run an update with that query, the update should NOT be applied, because it
            # should re-check that the object still matches the query
            queryset.update(is_mouldy=True)
        obj = TestFruit.objects.get(pk=obj.pk)
        self.assertFalse(obj.is_mouldy)

    @skipIf(django.VERSION < (1, 8), "DurationField only applies to Django <= 1.8")
    def test_duration_field_stored_as_float(self):
        """ See issue #512.  We have a bug report that the DurationField comes back as None when
            the value is set to a particular value which is roughly 3 days. This is caused by it
            being stored as a float instead of an int in the DB.
        """
        td2 = datetime.timedelta(days=2)
        # If the duration value is stored as a float instead of an int then this particular duration
        # will cause django.db.backends.base.operations.BaseDatabaseOperations.convert_durationfield_value
        # to return the value as None
        td3 = datetime.timedelta(days=3, seconds=14658, microseconds=886540)
        durations_as_2 = DurationModel.objects.create(
            duration_field=td2,
            duration_field_nullable=td2
        )
        durations_as_3 = DurationModel.objects.create(
            duration_field=td3,
            duration_field_nullable=td3
        )
        self.assertEqual(durations_as_2.duration_field, td2)
        self.assertEqual(durations_as_2.duration_field_nullable, td2)
        self.assertEqual(durations_as_3.duration_field, td3)
        self.assertEqual(durations_as_3.duration_field_nullable, td3)
        durations_as_2 = DurationModel.objects.get(pk=durations_as_2.pk)
        durations_as_3 = DurationModel.objects.get(pk=durations_as_3.pk)
        self.assertEqual(durations_as_2.duration_field, td2)
        self.assertEqual(durations_as_2.duration_field_nullable, td2)
        self.assertEqual(durations_as_3.duration_field, td3)
        self.assertEqual(durations_as_3.duration_field_nullable, td3)
        # And just for good measure, check the raw value in the datastore
        key = rpc.Key.from_path(DurationModel._meta.db_table, durations_as_3.pk, namespace=DEFAULT_NAMESPACE)
        entity = rpc.Get(key)
        self.assertTrue(isinstance(entity['duration_field'], (int, long)))

    def test_datetime_and_time_fields_precision_for_projection_queries(self):
        """
        The returned datetime and time values should include microseconds.
        See issue #707.
        """
        t = datetime.time(22, 13, 50, 541022)
        dt = datetime.datetime(2016, 5, 27, 18, 40, 12, 927371)
        NullDate.objects.create(time=t, datetime=dt)
        result = NullDate.objects.all().values_list('time', 'datetime')
        expected = [(t, dt)]
        self.assertItemsEqual(result, expected)

    def test_filter_with_empty_q(self):
        t1 = TestUser.objects.create(username='foo', field2='bar')
        condition = Q() | Q(username='foo')
        self.assertEqual(t1, TestUser.objects.filter(condition).first())

        condition = Q()
        self.assertEqual(t1, TestUser.objects.filter(condition).first())

    def test_only_defer_does_project(self):
        with sleuth.watch("djangae.db.backends.appengine.rpc.Query.__init__") as watcher:
            list(TestUser.objects.only("pk").all())
            self.assertTrue(watcher.calls[0].kwargs["keys_only"])
            self.assertFalse(watcher.calls[0].kwargs["projection"])

        with sleuth.watch("djangae.db.backends.appengine.rpc.Query.__init__") as watcher:
            list(TestUser.objects.values("pk"))
            self.assertTrue(watcher.calls[0].kwargs["keys_only"])
            self.assertFalse(watcher.calls[0].kwargs["projection"])

        with sleuth.watch("djangae.db.backends.appengine.rpc.Query.__init__") as watcher:
            list(TestUser.objects.only("username").all())
            self.assertFalse(watcher.calls[0].kwargs["keys_only"])
            self.assertItemsEqual(watcher.calls[0].kwargs["projection"], ["username"])

        with sleuth.watch("djangae.db.backends.appengine.rpc.Query.__init__") as watcher:
            list(TestUser.objects.defer("username").all())
            self.assertFalse(watcher.calls[0].kwargs["keys_only"])
            self.assertTrue(watcher.calls[0].kwargs["projection"])
            self.assertFalse("username" in watcher.calls[0].kwargs["projection"])

    def test_chaining_none_filter(self):
        t1 = TestUser.objects.create()
        self.assertFalse(TestUser.objects.none().filter(pk=t1.pk))

    def test_values_list_returns_unicode_strings(self):
        TestUser.objects.create(username=u"Łukasz")
        self.assertEqual(unicode, type(TestUser.objects.get().username))
        self.assertEqual(unicode, type(TestUser.objects.values_list("username", flat=True)[0]))


class ModelFormsetTest(TestCase):
    def test_reproduce_index_error(self):
        class TestModelForm(ModelForm):
            class Meta:
                model = TestUser
                fields = ("username", "email", "field2")

        test_model = TestUser.objects.create(username='foo', field2='bar')
        TestModelFormSet = modelformset_factory(TestUser, form=TestModelForm, extra=0)
        TestModelFormSet(queryset=TestUser.objects.filter(pk=test_model.pk))

        data = {
            'form-INITIAL_FORMS': 0,
            'form-MAX_NUM_FORMS': 0,
            'form-TOTAL_FORMS': 0,
            'form-0-id': test_model.id,
            'form-0-field1': 'foo_1',
            'form-0-field2': 'bar_1',
        }
        factory = RequestFactory()
        request = factory.post('/', data=data)

        TestModelFormSet(request.POST, request.FILES)


class CacheTests(TestCase):

    def test_cache_set(self):
        cache.set('test?', 'yes!')
        self.assertEqual(cache.get('test?'), 'yes!')

    def test_cache_timeout(self):
        cache.set('test?', 'yes!', 1)
        import time
        time.sleep(1)
        self.assertEqual(cache.get('test?'), None)


def compare_markers(list1, list2):
    return (
        sorted([(x.key(), x.instance) for x in list1]) == sorted([(x.key(), x.instance) for x in list2])
    )


class ConstraintTests(TestCase):
    """
        Tests for unique constraint handling
    """

    def test_transaction_failure_to_apply(self):
        """
            This test simulates a failure to apply a transaction when saving an
            entity. The mocked function allows independent transactions to work
            normally so that we are testing what happens when markers can be created
            (which use independent transactions) but the outer transaction fails
        """
        original_commit = datastore_rpc.TransactionalConnection.commit

        def fake_commit(self, *args, **kwargs):
            config = self._BaseConnection__config

            # Do the normal thing on the constraint's independent transaction, but
            # fail otherwise
            if config.propagation == datastore_rpc.TransactionOptions.INDEPENDENT:
                return original_commit(self, *args, **kwargs)
            return False

        initial_constraints = list(UniqueMarker.all())
        with sleuth.switch(
            'google.appengine.datastore.datastore_rpc.TransactionalConnection.commit', fake_commit
        ) as commit:
            self.assertRaises(TransactionFailedError, ModelWithUniques.objects.create, name="One")
            self.assertTrue(commit.called)

        # Constraints should be the same
        self.assertTrue(compare_markers(initial_constraints, UniqueMarker.all()))

        instance = ModelWithUniques.objects.create(name="One")
        initial_constraints = list(UniqueMarker.all())

        with sleuth.switch(
            'google.appengine.datastore.datastore_rpc.TransactionalConnection.commit', fake_commit
        ) as commit:
            instance.name = "Two"
            self.assertRaises(TransactionFailedError, instance.save)
            self.assertTrue(commit.called)

        # Constraints should be the same
        self.assertTrue(compare_markers(initial_constraints, UniqueMarker.all()))

    def test_marker_creation_transaction_failure(self):
        """
            This test simulates a failure to apply a transaction when saving an
            entity. The mocked function prevents independent transactions from working
            meaning that markers can't be acquired or released. This should force
            any outer transaction to rollback
        """

        original_commit = datastore_rpc.TransactionalConnection.commit

        def fake_commit(self, *args, **kwargs):
            config = self._BaseConnection__config

            # Blow up on independent transactions
            if config.propagation != datastore_rpc.TransactionOptions.INDEPENDENT:
                return original_commit(self, *args, **kwargs)
            return False

        initial_constraints = list(UniqueMarker.all())
        with sleuth.switch(
            'google.appengine.datastore.datastore_rpc.TransactionalConnection.commit', fake_commit
        ) as commit:
            self.assertRaises(TransactionFailedError, ModelWithUniques.objects.create, name="One")
            self.assertTrue(commit.called)

        # Constraints should be the same
        self.assertTrue(compare_markers(initial_constraints, UniqueMarker.all()))
        self.assertRaises(ModelWithUniques.DoesNotExist, ModelWithUniques.objects.get, name="One")

        instance = ModelWithUniques.objects.create(name="One")
        initial_constraints = list(UniqueMarker.all())

        with sleuth.switch(
            'google.appengine.datastore.datastore_rpc.TransactionalConnection.commit', fake_commit
        ) as commit:
            instance.name = "Two"
            self.assertRaises(TransactionFailedError, instance.save)
            self.assertTrue(commit.called)

        # Constraints should be the same
        self.assertTrue(compare_markers(initial_constraints, UniqueMarker.all()))
        self.assertRaises(ModelWithUniques.DoesNotExist, ModelWithUniques.objects.get, name="Two")
        self.assertEqual(instance, ModelWithUniques.objects.get(name="One"))

    def test_update_updates_markers(self):
        initial_count = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count()

        instance = ModelWithUniques.objects.create(name="One")

        self.assertEqual(
            1,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )

        qry = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE)
        qry.Order(("created", rpc.Query.DESCENDING))

        marker = [x for x in qry.Run()][0]
        # Make sure we assigned the instance
        self.assertEqual(
            marker["instance"],
            rpc.Key.from_path(instance._meta.db_table, instance.pk, namespace=DEFAULT_NAMESPACE)
        )

        expected_marker = "{}|name:{}".format(ModelWithUniques._meta.db_table, md5("One").hexdigest())
        self.assertEqual(expected_marker, marker.key().id_or_name())

        instance.name = "Two"
        instance.save()

        self.assertEqual(
            1,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )
        marker = [x for x in qry.Run()][0]
        # Make sure we assigned the instance
        self.assertEqual(
            marker["instance"],
            rpc.Key.from_path(instance._meta.db_table, instance.pk, namespace=DEFAULT_NAMESPACE)
        )

        expected_marker = "{}|name:{}".format(ModelWithUniques._meta.db_table, md5("Two").hexdigest())
        self.assertEqual(expected_marker, marker.key().id_or_name())

    def test_conflicting_insert_throws_integrity_error(self):
        try:
            constraints.UNOWNED_MARKER_TIMEOUT_IN_SECONDS = 0
            ModelWithUniques.objects.create(name="One")

            with self.assertRaises(IntegrityError):
                ModelWithUniques.objects.create(name="One")

            # An insert with a specified ID enters a different code path
            # so we need to ensure it works
            ModelWithUniques.objects.create(id=555, name="Two")

            with self.assertRaises(IntegrityError):
                ModelWithUniques.objects.create(name="Two")

            # Make sure that bulk create works properly
            ModelWithUniques.objects.bulk_create([
                ModelWithUniques(name="Three"),
                ModelWithUniques(name="Four"),
                ModelWithUniques(name="Five"),
            ])

            with self.assertRaises(IntegrityError):
                ModelWithUniques.objects.create(name="Four")

            with self.assertRaises(NotSupportedError):
                # Make sure bulk creates are limited when there are unique constraints
                # involved
                ModelWithUniques.objects.bulk_create(
                    [ModelWithUniques(name=str(x)) for x in range(26)]
                )

        finally:
            constraints.UNOWNED_MARKER_TIMEOUT_IN_SECONDS = 5

    def test_integrity_error_message_correct(self):
        """ Check that the IntegrityError messages mentions the correct field(s). """

        # Create a conflict on `unique_field`
        obj1 = UniqueModel.objects.create(unique_field="One")
        try:
            UniqueModel.objects.create(unique_field="One", unique_combo_one=1)
        except IntegrityError as e:
            self.assertTrue("unique_field" in unicode(e))

        # Create a conflict on `unique_relation`
        UniqueModel.objects.create(unique_relation=obj1, unique_field="two", unique_combo_one=2)
        try:
            UniqueModel.objects.create(unique_relation=obj1, unique_field="three", unique_combo_one=3)
        except IntegrityError as e:
            self.assertTrue("unique_relation" in unicode(e))

        # Create a conflict on a unique_together combo`
        UniqueModel.objects.create(unique_field="four", unique_combo_one=4, unique_combo_two="five")
        try:
            UniqueModel.objects.create(unique_field="five", unique_combo_one=4, unique_combo_two="five")
        except IntegrityError as e:
            self.assertTrue("unique_combo_one" in unicode(e))
            self.assertTrue("unique_combo_two" in unicode(e))

    def test_table_flush_clears_markers_for_that_table(self):
        ModelWithUniques.objects.create(name="One")
        UniqueModel.objects.create(unique_field="One")

        FlushCommand(ModelWithUniques._meta.db_table, default_connection).execute()

        ModelWithUniques.objects.create(name="One")

        with self.assertRaises(IntegrityError):
            UniqueModel.objects.create(unique_field="One")

    def test_recently_deleted_unique_doesnt_come_back(self):
        instance = ModelWithUniques.objects.create(name="One")

        with inconsistent_db():
            instance.delete()
            self.assertEqual(0, ModelWithUniques.objects.filter(name="One").count())
            self.assertFalse(ModelWithUniques.objects.filter(name="One").exists())
            self.assertFalse(list(ModelWithUniques.objects.all()))  # Triple-check

    def test_conflicting_update_throws_integrity_error(self):
        ModelWithUniques.objects.create(name="One")

        instance = ModelWithUniques.objects.create(name="Two")
        with self.assertRaises(IntegrityError):
            instance.name = "One"
            instance.save()

    def test_existing_marker_replaced_if_nonexistent_instance(self):
        stale_instance = ModelWithUniques.objects.create(name="One")

        # Delete the entity without updating the markers
        key = rpc.Key.from_path(ModelWithUniques._meta.db_table, stale_instance.pk, namespace=DEFAULT_NAMESPACE)
        rpc.Delete(key)

        ModelWithUniques.objects.create(name="One") # Should be fine
        with self.assertRaises(IntegrityError):
            ModelWithUniques.objects.create(name="One")

    def test_unique_combinations_are_returned_correctly(self):
        combos_one = _unique_combinations(ModelWithUniquesOnForeignKey, ignore_pk=True)
        combos_two = _unique_combinations(ModelWithUniquesOnForeignKey, ignore_pk=False)

        self.assertEqual([['name', 'related_name'], ['name'], ['related_name']], combos_one)
        self.assertEqual([['name', 'related_name'], ['id'], ['name'], ['related_name']], combos_two)

        class Entity(dict):
            def __init__(self, model, id):
                self._key = rpc.Key.from_path(model, id, namespace=DEFAULT_NAMESPACE)

            def key(self):
                return self._key

        e1 = Entity(ModelWithUniquesOnForeignKey._meta.db_table, 1)
        e1["name"] = "One"
        e1["related_name_id"] = 1

        ids_one = unique_identifiers_from_entity(ModelWithUniquesOnForeignKey, e1)

        self.assertItemsEqual([
            u'djangae_modelwithuniquesonforeignkey|id:1',
            u'djangae_modelwithuniquesonforeignkey|name:06c2cea18679d64399783748fa367bdd',
            u'djangae_modelwithuniquesonforeignkey|related_name_id:1',
            u'djangae_modelwithuniquesonforeignkey|name:06c2cea18679d64399783748fa367bdd|related_name_id:1'
        ], ids_one)

    def test_error_on_update_doesnt_change_markers(self):
        initial_count = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count()

        instance = ModelWithUniques.objects.create(name="One")

        self.assertEqual(
            1,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )

        qry = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE)
        qry.Order(("created", rpc.Query.DESCENDING))

        marker = [x for x in qry.Run()][0]

        # Make sure we assigned the instance
        self.assertEqual(
            marker["instance"],
            rpc.Key.from_path(instance._meta.db_table, instance.pk, namespace=DEFAULT_NAMESPACE)
        )

        expected_marker = "{}|name:{}".format(ModelWithUniques._meta.db_table, md5("One").hexdigest())
        self.assertEqual(expected_marker, marker.key().id_or_name())

        instance.name = "Two"

        def wrapped_put(*args, **kwargs):
            kind = args[0][0].kind() if isinstance(args[0], list) else args[0].kind()
            if kind != UniqueMarker.kind():
                raise AssertionError()
            return rpc.Put(*args, **kwargs)

        with sleuth.switch("djangae.db.backends.appengine.commands.rpc.Put", wrapped_put):
            with self.assertRaises(Exception):
                instance.save()

        self.assertEqual(
            1,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )
        marker = [x for x in qry.Run()][0]
        # Make sure we assigned the instance
        self.assertEqual(
            marker["instance"],
            rpc.Key.from_path(instance._meta.db_table, instance.pk, namespace=DEFAULT_NAMESPACE)
        )

        expected_marker = "{}|name:{}".format(ModelWithUniques._meta.db_table, md5("One").hexdigest())
        self.assertEqual(expected_marker, marker.key().id_or_name())

    def test_error_on_insert_doesnt_create_markers(self):
        initial_count = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count()

        def wrapped_put(*args, **kwargs):
            kind = args[0][0].kind() if isinstance(args[0], list) else args[0].kind()
            if kind != UniqueMarker.kind():
                raise AssertionError()
            return rpc.Put(*args, **kwargs)

        with sleuth.switch("djangae.db.backends.appengine.commands.rpc.Put", wrapped_put):
            with self.assertRaises(Exception):
                ModelWithUniques.objects.create(name="One")

        self.assertEqual(
            0,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )

    def test_delete_clears_markers(self):
        initial_count = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count()

        instance = ModelWithUniques.objects.create(name="One")
        self.assertEqual(
            1,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )
        instance.delete()
        self.assertEqual(
            0,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )

    @override_settings(DJANGAE_DISABLE_CONSTRAINT_CHECKS=True)
    def test_constraints_disabled_doesnt_create_or_check_markers(self):
        initial_count = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count()

        instance1 = ModelWithUniques.objects.create(name="One")

        self.assertEqual(
            initial_count,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count()
        )

        instance2 = ModelWithUniques.objects.create(name="One")

        self.assertEqual(instance1.name, instance2.name)
        self.assertFalse(instance1 == instance2)

    @override_settings(DJANGAE_DISABLE_CONSTRAINT_CHECKS=True)
    def test_constraints_can_be_enabled_per_model(self):

        initial_count = rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count()
        ModelWithUniquesAndOverride.objects.create(name="One")

        self.assertEqual(
            1,
            rpc.Query(UniqueMarker.kind(), namespace=DEFAULT_NAMESPACE).Count() - initial_count
        )

    def test_list_field_unique_constaints(self):
        instance1 = UniqueModel.objects.create(unique_field=1, unique_combo_one=1, unique_list_field=["A", "C"])

        with self.assertRaises((IntegrityError, DataError)):
            UniqueModel.objects.create(unique_field=2, unique_combo_one=2, unique_list_field=["A"])

        instance2 = UniqueModel.objects.create(unique_field=2, unique_combo_one=2, unique_list_field=["B"])

        instance2.unique_list_field = instance1.unique_list_field

        with self.assertRaises((IntegrityError, DataError)):
            instance2.save()

        instance1.unique_list_field = []
        instance1.save()

        instance2.save()

    def test_list_field_unique_constraints_validation(self):
        instance1 = UniqueModel(
            unique_set_field={"A"},
            unique_together_list_field=[1],
            unique_field=1,
            unique_combo_one=1,
            unique_list_field=["A", "C"]
        )

        # Without a custom mixin, Django can't construct a unique validation query for a list field
        self.assertRaises(ValueError, instance1.full_clean)
        UniqueModel.__bases__ = (UniquenessMixin,) + UniqueModel.__bases__
        instance1.full_clean()
        instance1.save()

        # Check the uniqueness mixing works with long lists
        instance1.unique_list_field = [x for x in range(31)]
        try:
            instance1.full_clean()
        except NotSupportedError:
            self.fail("Couldn't run unique check on long list field")
            return

        instance2 = UniqueModel(
            unique_set_field={"B"},
            unique_together_list_field=[2],
            unique_field=2,
            unique_combo_one=2,
            unique_list_field=["B", "C"]  # duplicate value C!
        )

        self.assertRaises(ValidationError, instance2.full_clean)
        UniqueModel.__bases__ = (models.Model,)

    def test_set_field_unique_constraints(self):
        instance1 = UniqueModel.objects.create(unique_field=1, unique_combo_one=1, unique_set_field={"A", "C"})

        with self.assertRaises((IntegrityError, DataError)):
            UniqueModel.objects.create(unique_field=2, unique_combo_one=2, unique_set_field={"A"})

        instance2 = UniqueModel.objects.create(unique_field=2, unique_combo_one=2, unique_set_field={"B"})

        instance2.unique_set_field = instance1.unique_set_field

        with self.assertRaises((IntegrityError, DataError)):
            instance2.save()

        instance1.unique_set_field = set()
        instance1.save()

        instance2.save()

        instance2.unique_set_field = set()
        instance2.save()  # You can have two fields with empty sets

    def test_unique_constraints_on_model_with_long_str_pk(self):
        """ Check that an object with a string-based PK of 500 characters (the max that GAE allows)
            can still have unique constraints pointing at it.  (See #242.)
        """
        obj = UniqueModelWithLongPK(pk="x" * 500, unique_field=1)
        obj.save()
        duplicate = UniqueModelWithLongPK(pk="y" * 500, unique_field=1)
        self.assertRaises(IntegrityError, duplicate.save)


class EdgeCaseTests(TestCase):
    def setUp(self):
        super(EdgeCaseTests, self).setUp()

        add_special_index(TestUser, "username", IExactIndexer(), "iexact")

        self.u1 = TestUser.objects.create(
            username="A",
            email="test@example.com",
            last_login=datetime.datetime.now().date(),
            id=1
        )

        self.u2 = TestUser.objects.create(
            username="B",
            email="test@example.com",
            last_login=datetime.datetime.now().date(),
            id=2
        )

        self.u3 = TestUser.objects.create(
            username="C",
            email="test2@example.com",
            last_login=datetime.datetime.now().date(),
            id=3
        )

        self.u4 = TestUser.objects.create(
            username="D",
            email="test3@example.com",
            last_login=datetime.datetime.now().date(),
            id=4
        )

        self.u5 = TestUser.objects.create(
            username="E",
            email="test3@example.com",
            last_login=datetime.datetime.now().date(),
            id=5
        )

        self.apple = TestFruit.objects.create(name="apple", color="red")
        self.banana = TestFruit.objects.create(name="banana", color="yellow")

    def test_querying_by_date(self):
        instance1 = ModelWithDates.objects.create(start=datetime.date(2014, 1, 1), end=datetime.date(2014, 1, 20))
        instance2 = ModelWithDates.objects.create(start=datetime.date(2014, 2, 1), end=datetime.date(2014, 2, 20))

        self.assertEqual(instance1, ModelWithDates.objects.get(start__lt=datetime.date(2014, 1, 2)))
        self.assertEqual(2, ModelWithDates.objects.filter(start__lt=datetime.date(2015, 1, 1)).count())

        self.assertEqual(instance2, ModelWithDates.objects.get(start__gt=datetime.date(2014, 1, 2)))
        self.assertEqual(instance2, ModelWithDates.objects.get(start__gte=datetime.date(2014, 2, 1)))

    def projection_plus_keys_filtering(self):
        """
            If you do a query like this:

            MyModel.objects.filter(pk__in=[1, 2]).filter(field1="Bananas").values_list("id", "someotherfield")

            Then a projection query is run. The problem is that the entities returned only include
            "id" and "someotherfield"
            but not "field1". Our entity-matches-query code should not run in this situation as we pass
            all filters to the ancestor queries and so any entities returned should match.
        """

        user = TestUser.objects.create(username="test", email="test@example.com")

        self.assertItemsEqual(
            [(user.pk, user.username)],
            TestUser.objects.filter(
                pk__in=[user.pk, user.pk + 1]
            ).filter(
                email="test@example.com"
            ).values_list("id", "username")
        )

    def test_double_starts_with(self):
        qs = TestUser.objects.filter(
            username__startswith='Hello'
        ) | TestUser.objects.filter(username__startswith='Goodbye')

        self.assertEqual(0, qs.count())

        TestUser.objects.create(username="Hello")
        self.assertEqual(1, qs.count())

        TestUser.objects.create(username="Goodbye")
        self.assertEqual(2, qs.count())

        TestUser.objects.create(username="Hello and Goodbye")
        self.assertEqual(3, qs.count())

    def test_impossible_starts_with(self):
        TestUser.objects.create(username="Hello")
        TestUser.objects.create(username="Goodbye")
        TestUser.objects.create(username="Hello and Goodbye")

        qs = TestUser.objects.filter(
            username__startswith='Hello'
        ) & TestUser.objects.filter(username__startswith='Goodbye')
        self.assertEqual(0, qs.count())

    def test_datetime_contains(self):
        """
            Django allows for __contains on datetime field, so that you can search for a specific
            date. This is probably just because SQL allows querying it on a string, and contains just
            turns into a like query. This test just makes sure we behave the same
        """

        instance = DateTimeModel.objects.create() # Create a DateTimeModel, it has auto_now stuff

        # Make sure that if we query a datetime on a date it is properly returned
        self.assertItemsEqual(
            [instance],
            DateTimeModel.objects.filter(
                datetime_field__contains=instance.datetime_field.date()
            )
        )
        self.assertItemsEqual([instance], DateTimeModel.objects.filter(date_field__contains=instance.date_field.year))

    def test_combinations_of_special_indexes(self):
        qs = TestUser.objects.filter(username__iexact='Hello') | TestUser.objects.filter(username__contains='ood')

        self.assertEqual(0, qs.count())

        TestUser.objects.create(username="Hello")
        self.assertEqual(1, qs.count())

        TestUser.objects.create(username="Goodbye")
        self.assertEqual(2, qs.count())

        TestUser.objects.create(username="Hello and Goodbye")
        self.assertEqual(3, qs.count())

    def test_multi_table_inheritance(self):

        parent = MultiTableParent.objects.create(parent_field="parent1")
        child1 = MultiTableChildOne.objects.create(parent_field="child1", child_one_field="child1")
        child2 = MultiTableChildTwo.objects.create(parent_field="child2", child_two_field="child2")

        self.assertEqual(3, MultiTableParent.objects.count())
        self.assertItemsEqual([parent.pk, child1.pk, child2.pk],
            list(MultiTableParent.objects.values_list('pk', flat=True)))
        self.assertEqual(1, MultiTableChildOne.objects.count())
        self.assertEqual(child1, MultiTableChildOne.objects.get())

        self.assertEqual(1, MultiTableChildTwo.objects.count())
        self.assertEqual(child2, MultiTableChildTwo.objects.get())

        self.assertEqual(child2, MultiTableChildTwo.objects.get(pk=child2.pk))
        self.assertTrue(MultiTableParent.objects.filter(pk=child2.pk).exists())

    def test_anding_pks(self):
        results = TestUser.objects.filter(id__exact=self.u1.pk).filter(id__exact=self.u2.pk)
        self.assertEqual(list(results), [])

    def test_unusual_queries(self):

        results = TestFruit.objects.filter(name__in=["apple", "orange"])
        self.assertEqual(1, len(results))
        self.assertItemsEqual(["apple"], [x.name for x in results])

        results = TestFruit.objects.filter(name__in=["apple", "banana"])
        self.assertEqual(2, len(results))
        self.assertItemsEqual(["apple", "banana"], [x.name for x in results])

        results = TestFruit.objects.filter(name__in=["apple", "banana"]).values_list('pk', 'color')
        self.assertEqual(2, len(results))
        self.assertItemsEqual([(self.apple.pk, self.apple.color), (self.banana.pk, self.banana.color)], results)

        results = TestUser.objects.all()
        self.assertEqual(5, len(results))

        results = TestUser.objects.filter(username__in=["A", "B"])
        self.assertEqual(2, len(results))
        self.assertItemsEqual(["A", "B"], [x.username for x in results])

        results = TestUser.objects.filter(username__in=["A", "B"]).exclude(username="A")
        self.assertEqual(1, len(results), results)
        self.assertItemsEqual(["B"], [x.username for x in results])

        results = TestUser.objects.filter(username__lt="E")
        self.assertEqual(4, len(results))
        self.assertItemsEqual(["A", "B", "C", "D"], [x.username for x in results])

        results = TestUser.objects.filter(username__lte="E")
        self.assertEqual(5, len(results))

        # Double exclude on different properties not supported
        with self.assertRaises(NotSupportedError):
            # FIXME: This should raise a NotSupportedError, but at the moment it's thrown too late in
            # the process and so Django wraps it as a DataError
            list(TestUser.objects.exclude(username="E").exclude(email="A"))

        results = list(TestUser.objects.exclude(username="E").exclude(username="A"))
        self.assertItemsEqual(["B", "C", "D"], [x.username for x in results])

        results = TestUser.objects.filter(username="A", email="test@example.com")
        self.assertEqual(1, len(results))

        results = TestUser.objects.filter(username__in=["A", "B"]).filter(username__in=["A", "B"])
        self.assertEqual(2, len(results))
        self.assertItemsEqual(["A", "B"], [x.username for x in results])

        results = TestUser.objects.filter(username__in=["A", "B"]).filter(username__in=["A"])
        self.assertEqual(1, len(results))
        self.assertItemsEqual(["A"], [x.username for x in results])

        results = TestUser.objects.filter(pk__in=[self.u1.pk, self.u2.pk]).filter(username__in=["A"])
        self.assertEqual(1, len(results))
        self.assertItemsEqual(["A"], [x.username for x in results])

        results = TestUser.objects.filter(username__in=["A"]).filter(pk__in=[self.u1.pk, self.u2.pk])
        self.assertEqual(1, len(results))
        self.assertItemsEqual(["A"], [x.username for x in results])

        results = list(TestUser.objects.all().exclude(username__in=["A"]))
        self.assertItemsEqual(["B", "C", "D", "E"], [x.username for x in results])

        results = list(TestFruit.objects.filter(name='apple', color__in=[]))
        self.assertItemsEqual([], results)

        results = list(TestUser.objects.all().exclude(username__in=[]))
        self.assertEqual(5, len(results))
        self.assertItemsEqual(["A", "B", "C", "D", "E"], [x.username for x in results])

        results = list(TestUser.objects.all().exclude(username__in=[]).filter(username__in=["A", "B"]))
        self.assertEqual(2, len(results))
        self.assertItemsEqual(["A", "B"], [x.username for x in results])

        results = list(TestUser.objects.all().filter(username__in=["A", "B"]).exclude(username__in=[]))
        self.assertEqual(2, len(results))
        self.assertItemsEqual(["A", "B"], [x.username for x in results])

    def test_empty_string_key(self):
        # Creating
        with self.assertRaises(IntegrityError):
            TestFruit.objects.create(name='')

        # Getting
        with self.assertRaises(TestFruit.DoesNotExist):
            TestFruit.objects.get(name='')

        # Filtering
        results = list(TestFruit.objects.filter(name='').order_by("name"))
        self.assertItemsEqual([], results)

        # Combined filtering
        results = list(TestFruit.objects.filter(name='', color='red').order_by("name"))
        self.assertItemsEqual([], results)

        # IN query
        results = list(TestFruit.objects.filter(name__in=['', 'apple']))
        self.assertItemsEqual([self.apple], results)

    def test_or_queryset(self):
        """
            This constructs an OR query, this is currently broken in the parse_where_and_check_projection
            function. WE MUST FIX THIS!
        """
        q1 = TestUser.objects.filter(username="A")
        q2 = TestUser.objects.filter(username="B")

        self.assertItemsEqual([self.u1, self.u2], list(q1 | q2))

    def test_or_q_objects(self):
        """ Test use of Q objects in filters. """
        query = TestUser.objects.filter(Q(username="A") | Q(username="B"))
        self.assertItemsEqual([self.u1, self.u2], list(query))

    def test_extra_select(self):
        results = TestUser.objects.filter(username='A').extra(select={'is_a': "username = 'A'"})
        self.assertEqual(1, len(results))
        self.assertItemsEqual([True], [x.is_a for x in results])

        results = TestUser.objects.all().exclude(username='A').extra(select={'is_a': "username = 'A'"})
        self.assertEqual(4, len(results))
        self.assertEqual(not any([x.is_a for x in results]), True)

        # Up for debate
        # results = User.objects.all().extra(select={'truthy': 'TRUE'})
        # self.assertEqual(all([x.truthy for x in results]), True)

        results = TestUser.objects.all().extra(select={'truthy': True})
        self.assertEqual(all([x.truthy for x in results]), True)

    def test_counts(self):
        self.assertEqual(5, TestUser.objects.count())
        self.assertEqual(2, TestUser.objects.filter(email="test3@example.com").count())
        self.assertEqual(3, TestUser.objects.exclude(email="test3@example.com").count())
        self.assertEqual(1, TestUser.objects.filter(username="A").exclude(email="test3@example.com").count())
        self.assertEqual(3, TestUser.objects.exclude(username="E").exclude(username="A").count())

        self.assertEqual(3, TestUser.objects.exclude(username__in=["A", "B"]).count())
        self.assertEqual(0, TestUser.objects.filter(email="test@example.com").exclude(username__in=["A", "B"]).count())

    def test_exclude_with__in(self):
        self.assertEqual(
            set([self.u3, self.u4, self.u5]),
            set(list(TestUser.objects.exclude(username__in=["A", "B"])))
        )

    def test_deletion(self):
        count = TestUser.objects.count()
        self.assertTrue(count)

        TestUser.objects.filter(username="A").delete()
        self.assertEqual(count - 1, TestUser.objects.count())

        TestUser.objects.filter(username="B").exclude(username="B").delete() # Should do nothing
        self.assertEqual(count - 1, TestUser.objects.count())

        TestUser.objects.all().delete()
        count = TestUser.objects.count()
        self.assertFalse(count)

    def test_double_delete(self):
        u1 = TestUser.objects.get(username="A")
        u2 = TestUser.objects.get(username="A")

        u1.delete()
        u2.delete()

    def test_insert_with_existing_key(self):
        user = TestUser.objects.create(id=999, username="test1", last_login=datetime.datetime.now().date())
        self.assertEqual(999, user.pk)

        with self.assertRaises(IntegrityError):
            TestUser.objects.create(id=999, username="test2", last_login=datetime.datetime.now().date())

    def test_included_pks(self):
        ids = [TestUser.objects.get(username="B").pk, TestUser.objects.get(username="A").pk]
        results = TestUser.objects.filter(pk__in=ids).order_by("username")

        self.assertEqual(results[0], self.u1)
        self.assertEqual(results[1], self.u2)

    def test_select_related(self):
        """ select_related should be a no-op... for now """
        user = TestUser.objects.get(username="A")
        Permission.objects.create(user=user, perm="test_perm")
        select_related = [(p.perm, p.user.username) for p in user.permission_set.select_related()]
        self.assertEqual(user.username, select_related[0][1])

    def test_cross_selects(self):
        user = TestUser.objects.get(username="A")
        Permission.objects.create(user=user, perm="test_perm")
        with self.assertRaises(NotSupportedError):
            perms = list(Permission.objects.all().values_list("user__username", "perm"))
            self.assertEqual("A", perms[0][0])

    def test_invalid_id_value_on_insert(self):
        user = TestUser.objects.get(username="A")
        # pass in a User object as if it's an int
        permission = Permission(user_id=user, perm="test_perm")
        with self.assertRaises(TypeError):
            permission.save(force_insert=True)

    def test_values_list_on_pk_does_keys_only_query(self):
        from google.appengine.api.datastore import Query

        def replacement_init(*args, **kwargs):
            replacement_init.called_args = args
            replacement_init.called_kwargs = kwargs
            original_init(*args, **kwargs)

        replacement_init.called_args = None
        replacement_init.called_kwargs = None

        try:
            original_init = Query.__init__
            Query.__init__ = replacement_init
            list(TestUser.objects.all().values_list('pk', flat=True))
        finally:
            Query.__init__ = original_init

        self.assertTrue(replacement_init.called_kwargs.get('keys_only'))
        self.assertEqual(5, len(TestUser.objects.all().values_list('pk')))

    def test_iexact(self):
        user = TestUser.objects.get(username__iexact="a")
        self.assertEqual("A", user.username)

        add_special_index(IntegerModel, "integer_field", IExactIndexer(), "iexact")
        IntegerModel.objects.create(integer_field=1000)
        integer_model = IntegerModel.objects.get(integer_field__iexact=str(1000))
        self.assertEqual(integer_model.integer_field, 1000)

        user = TestUser.objects.get(id__iexact=str(self.u1.id))
        self.assertEqual("A", user.username)

    def test_iexact_containing_underscores(self):
        add_special_index(TestUser, "username", IExactIndexer(), "iexact")
        user = TestUser.objects.create(username="A_B", email="test@example.com")
        results = TestUser.objects.filter(username__iexact=user.username.lower())
        self.assertEqual(list(results), [user])

    def test_year(self):
        user = TestUser.objects.create(username="Z", email="z@example.com")
        user.last_login = datetime.datetime(2000, 1, 1, 0, 0, 0)
        user.save()

        self.assertEqual(len(TestUser.objects.filter(last_login__year=3000)), 0)
        self.assertEqual(TestUser.objects.filter(last_login__year=2000).first().pk, user.pk)

    def test_ordering(self):
        users = TestUser.objects.all().order_by("username")

        self.assertEqual(["A", "B", "C", "D", "E"], [x.username for x in users])

        users = TestUser.objects.all().order_by("-username")

        self.assertEqual(["A", "B", "C", "D", "E"][::-1], [x.username for x in users])

        with self.assertRaises(FieldError):
            users = list(TestUser.objects.order_by("bananas"))

        users = TestUser.objects.filter(id__in=[self.u2.id, self.u3.id, self.u4.id]).order_by('id')
        self.assertEqual(["B", "C", "D"], [x.username for x in users])

        users = TestUser.objects.filter(id__in=[self.u2.id, self.u3.id, self.u4.id]).order_by('-id')
        self.assertEqual(["D", "C", "B"], [x.username for x in users])

        users = TestUser.objects.filter(id__in=[self.u1.id, self.u5.id, self.u3.id]).order_by('id')
        self.assertEqual(["A", "C", "E"], [x.username for x in users])

        users = TestUser.objects.filter(id__in=[self.u4.id, self.u5.id, self.u3.id, self.u1.id]).order_by('-id')
        self.assertEqual(["E", "D", "C", "A"], [x.username for x in users])

    def test_dates_query(self):
        z_user = TestUser.objects.create(username="Z", email="z@example.com")
        z_user.last_login = datetime.date(2013, 4, 5)
        z_user.save()

        last_a_login = TestUser.objects.get(username="A").last_login

        dates = TestUser.objects.dates('last_login', 'year')

        self.assertItemsEqual(
            [datetime.date(2013, 1, 1), datetime.date(last_a_login.year, 1, 1)],
            dates
        )

        dates = TestUser.objects.dates('last_login', 'month')
        self.assertItemsEqual(
            [datetime.date(2013, 4, 1), datetime.date(last_a_login.year, last_a_login.month, 1)],
            dates
        )

        dates = TestUser.objects.dates('last_login', 'day')
        self.assertEqual(
            [datetime.date(2013, 4, 5), last_a_login],
            list(dates)
        )

        dates = TestUser.objects.dates('last_login', 'day', order='DESC')
        self.assertEqual(
            [last_a_login, datetime.date(2013, 4, 5)],
            list(dates)
        )

    @override_settings(DJANGAE_MAX_QUERY_BRANCHES=30)
    def test_in_query(self):
        """ Test that the __in filter works, and that it cannot be used with more than 30 values,
            unless it's used on the PK field.
        """
        # Check that a basic __in query works
        results = list(TestUser.objects.filter(username__in=['A', 'B']))
        self.assertItemsEqual(results, [self.u1, self.u2])
        # Check that it also works on PKs
        results = list(TestUser.objects.filter(pk__in=[self.u1.pk, self.u2.pk]))
        self.assertItemsEqual(results, [self.u1, self.u2])
        # Check that using more than 30 items in an __in query not on the pk causes death
        query = TestUser.objects.filter(username__in=list([x for x in letters[:31]]))
        self.assertRaises(Exception, list, query)
        # Check that it's ok with PKs though
        query = TestUser.objects.filter(pk__in=list(range(1, 32)))
        list(query)
        # Check that it's ok joining filters with pks
        results = list(TestUser.objects.filter(
            pk__in=[self.u1.pk, self.u2.pk, self.u3.pk]).filter(pk__in=[self.u1.pk, self.u2.pk]))
        self.assertItemsEqual(results, [self.u1, self.u2])

    def test_self_relations(self):
        obj = SelfRelatedModel.objects.create()
        obj2 = SelfRelatedModel.objects.create(related=obj)
        self.assertEqual(list(obj.selfrelatedmodel_set.all()), [obj2])

    def test_special_indexes_for_empty_fields(self):
        obj = TestFruit.objects.create(name='pear')
        indexes = ['icontains', 'contains', 'iexact', 'iendswith', 'endswith', 'istartswith', 'startswith']
        for index in indexes:
            add_special_index(TestFruit, 'color', get_indexer(TestFruit._meta.get_field("color"), index), index)
        obj.save()

    def test_special_indexes_for_unusually_long_values(self):
        obj = TestFruit.objects.create(name='pear', color='1234567890-=!@#$%^&*()_+qQWERwertyuiopasdfghjklzxcvbnm')
        indexes = ['icontains', 'contains', 'iexact', 'iendswith', 'endswith', 'istartswith', 'startswith']
        for index in indexes:
            add_special_index(TestFruit, 'color', get_indexer(TestFruit._meta.get_field("color"), index), index)
        obj.save()

        qry = TestFruit.objects.filter(color__contains='1234567890-=!@#$%^&*()_+qQWERwertyuiopasdfghjklzxcvbnm')
        self.assertEqual(len(list(qry)), 1)
        qry = TestFruit.objects.filter(color__contains='890-=!@#$')
        self.assertEqual(len(list(qry)), 1)
        qry = TestFruit.objects.filter(color__contains='1234567890-=!@#$%^&*()_+qQWERwertyui')
        self.assertEqual(len(list(qry)), 1)
        qry = TestFruit.objects.filter(color__contains='8901')
        self.assertEqual(len(list(qry)), 0)

        qry = TestFruit.objects.filter(color__icontains='1234567890-=!@#$%^&*()_+qQWERWERTYuiopasdfghjklzxcvbnm')
        self.assertEqual(len(list(qry)), 1)
        qry = TestFruit.objects.filter(color__icontains='890-=!@#$')
        self.assertEqual(len(list(qry)), 1)
        qry = TestFruit.objects.filter(color__icontains='1234567890-=!@#$%^&*()_+qQWERwertyuI')
        self.assertEqual(len(list(qry)), 1)
        qry = TestFruit.objects.filter(color__icontains='8901')
        self.assertEqual(len(list(qry)), 0)

    def test_values_list_on_distinct(self):
        TestFruit.objects.create(name="Kiwi", origin="New Zealand", color="Green")
        TestFruit.objects.create(name="Apple", origin="New Zealand", color="Green")
        TestFruit.objects.create(name="Grape", origin="New Zealand", color="Red")
        nz_colours = TestFruit.objects.filter(
            origin="New Zealand"
        ).distinct("color").values_list("color", flat=True)
        self.assertEqual(sorted(nz_colours), ["Green", "Red"])

    def test_empty_key_lookups_work_correctly(self):
        t1 = TestFruit.objects.create(name="Kiwi", origin="New Zealand", color="Green")
        TestFruit.objects.create(name="Apple", origin="New Zealand", color="Green")

        self.assertEqual(
            t1,
            TestFruit.objects.exclude(name="Apple").exclude(name="").get(name="Kiwi")
        )

        self.assertFalse(TestFruit.objects.filter(name="", color="Green"))
        self.assertTrue(TestFruit.objects.filter(Q(name="") | Q(name="Kiwi")).filter(color="Green"))
        self.assertFalse(TestFruit.objects.filter(name="", color__gt="A"))
        self.assertEqual(4, TestFruit.objects.exclude(name="").count())

    def test_additional_indexes_respected(self):
        project, additional = indexing._project_special_indexes.copy(), indexing._app_special_indexes.copy()

        try:
            indexing._project_special_indexes = {}
            indexing._app_special_indexes = {
                TestFruit._meta.db_table: {"name": ["iexact"]}
            }

            t1 = TestFruit.objects.create(name="Kiwi", origin="New Zealand", color="Green")
            self.assertEqual(t1, TestFruit.objects.filter(name__iexact="kiwi").get())
            self.assertFalse(indexing._project_special_indexes) # Nothing was added
        finally:
            indexing._project_special_indexes = project
            indexing._app_special_indexes = additional


class BlobstoreFileUploadHandlerTest(TestCase):
    boundary = "===============7417945581544019063=="

    def setUp(self):
        super(BlobstoreFileUploadHandlerTest, self).setUp()

        self.request = RequestFactory().get('/')
        ctype = 'message/external-body; blob-key="PLOF0qOie14jzHWJXEa9HA=="; access-type="X-AppEngine-BlobKey"'
        self.request.META = {
            'wsgi.input': self._create_wsgi_input(),
            'content-type': ctype
        }
        self.uploader = BlobstoreFileUploadHandler(self.request)
        self.extra_content_type = {'blob-key': 'PLOF0qOie14jzHWJXEa9HA==', 'access-type': 'X-AppEngine-BlobKey'}

    def _create_wsgi_input(self):
        return StringIO(u'--===============7417945581544019063==\r\nContent-Type:'
                        ' text/plain\r\nContent-Disposition: form-data;'
                        ' name="field-nationality"\r\n\r\nAS\r\n'
                        '--===============7417945581544019063==\r\nContent-Type:'
                        ' message/external-body; blob-key="PLOF0qOie14jzHWJXEa9HA==";'
                        ' access-type="X-AppEngine-BlobKey"\r\nContent-Disposition:'
                        ' form-data; name="field-file";'
                        ' filename="Scan.tiff"\r\n\r\nContent-Type: image/tiff'
                        '\r\nContent-Length: 19837164\r\nContent-MD5:'
                        ' YjI1M2Q5NjM5YzdlMzUxYjMyMjA0ZTIxZjAyNzdiM2Q=\r\ncontent-disposition:'
                        ' form-data; name="field-file";'
                        ' filename="Scan.tiff"\r\nX-AppEngine-Upload-Creation: 2014-03-07'
                        ' 14:48:03.246607\r\n\r\n\r\n'
                        '--===============7417945581544019063==\r\nContent-Type:'
                        ' text/plain\r\nContent-Disposition: form-data;'
                        ' name="field-number"\r\n\r\n6\r\n'
                        '--===============7417945581544019063==\r\nContent-Type:'
                        ' text/plain\r\nContent-Disposition: form-data;'
                        ' name="field-salutation"\r\n\r\nmrs\r\n'
                        '--===============7417945581544019063==--')

    def test_non_existing_files_do_not_get_created(self):
        file_field_name = 'field-file'
        length = len(self._create_wsgi_input().read())
        self.uploader.handle_raw_input(
            self.request.META['wsgi.input'],
            self.request.META, length, self.boundary, "utf-8"
        )
        self.assertRaises(StopFutureHandlers, self.uploader.new_file, file_field_name,
            'file_name', None, None, None, self.extra_content_type)
        self.assertRaises(EntityNotFoundError, self.uploader.file_complete, None)

    def test_blob_key_creation(self):
        file_field_name = 'field-file'
        length = len(self._create_wsgi_input().read())
        self.uploader.handle_raw_input(
            self.request.META['wsgi.input'],
            self.request.META, length, self.boundary, "utf-8"
        )
        self.assertRaises(
            StopFutureHandlers,
            self.uploader.new_file, file_field_name, 'file_name', None, None, None, self.extra_content_type
        )
        self.assertIsNotNone(self.uploader.blobkey)

    def test_blobstore_upload_url_templatetag(self):
        template = """{% load storage %}{% blobstore_upload_url '/something/' %}"""
        response = Template(template).render(Context({}))
        self.assertTrue(response.startswith("http://localhost:8080/_ah/upload/"))


class DatastorePaginatorTest(TestCase):

    def setUp(self):
        super(DatastorePaginatorTest, self).setUp()

        for i in range(15):
            PaginatorModel.objects.create(foo=i)

    def test_basic_usage(self):
        def qs():
            return PaginatorModel.objects.all().order_by('foo')

        p1 = paginator.DatastorePaginator(qs(), 5).page(1)
        self.assertFalse(p1.has_previous())
        self.assertTrue(p1.has_next())
        self.assertEqual(p1.start_index(), 1)
        self.assertEqual(p1.end_index(), 5)
        self.assertEqual(p1.next_page_number(), 2)
        self.assertEqual([x.foo for x in p1], [0, 1, 2, 3, 4])

        p2 = paginator.DatastorePaginator(qs(), 5).page(2)
        self.assertTrue(p2.has_previous())
        self.assertTrue(p2.has_next())
        self.assertEqual(p2.start_index(), 6)
        self.assertEqual(p2.end_index(), 10)
        self.assertEqual(p2.previous_page_number(), 1)
        self.assertEqual(p2.next_page_number(), 3)
        self.assertEqual([x.foo for x in p2], [5, 6, 7, 8, 9])

        p3 = paginator.DatastorePaginator(qs(), 5).page(3)
        self.assertTrue(p3.has_previous())
        self.assertFalse(p3.has_next())
        self.assertEqual(p3.start_index(), 11)
        self.assertEqual(p3.end_index(), 15)
        self.assertEqual(p3.previous_page_number(), 2)
        self.assertEqual([x.foo for x in p3], [10, 11, 12, 13, 14])

    def test_empty(self):
        qs = PaginatorModel.objects.none()
        p1 = paginator.DatastorePaginator(qs, 5).page(1)
        self.assertFalse(p1.has_previous())
        self.assertFalse(p1.has_next())
        self.assertEqual(p1.start_index(), 0)
        self.assertEqual(p1.end_index(), 0)
        self.assertEqual([x for x in p1], [])


class TestSpecialIndexers(TestCase):

    def setUp(self):
        super(TestSpecialIndexers, self).setUp()

        self.names = [
            'Ola', 'Adam', 'Luke', 'rob', 'Daniel', 'Ela', 'Olga', 'olek',
            'ola', 'Olaaa', 'OlaaA', 'Ola + Ola', '-Test-', '-test-'
        ]
        for name in self.names:
            SpecialIndexesModel.objects.create(name=name)

        self.lists = [
            self.names,
            ['Name', 'name', 'name + name'],
            ['-Tesst-'],
            ['-test-']
        ]
        for i, sample_list in enumerate(self.lists):
            SpecialIndexesModel.objects.create(name=i, sample_list=sample_list)

        self.qry = SpecialIndexesModel.objects.all()

    def test_iexact_lookup(self):
        for name in self.names:
            qry = self.qry.filter(name__iexact=name)
            self.assertEqual(len(qry), len([x for x in self.names if x.lower() == name.lower()]))

    def test_contains_lookup_and_icontains_lookup(self):
        tests = self.names + ['o', 'O', 'la']
        for name in tests:
            qry = self.qry.filter(name__contains=name)
            self.assertEqual(len(qry), len([x for x in self.names if name in x]))

            qry = self.qry.filter(name__icontains=name)
            self.assertEqual(len(qry), len([x for x in self.names if name.lower() in x.lower()]))

    def test_contains_lookup_on_charfield_subclass(self):
        """ Test that the __contains lookup also works on subclasses of the Django CharField, e.g.
            the custom Djangae CharField.
        """
        instance = SpecialIndexesModel.objects.create(name="whatever", nickname="Voldemort")
        query = SpecialIndexesModel.objects.filter(nickname__contains="demo")
        self.assertEqual(list(query), [instance])

    def test_endswith_lookup_and_iendswith_lookup(self):
        tests = self.names + ['a', 'A', 'aa']
        for name in tests:
            qry = self.qry.filter(name__endswith=name)
            self.assertEqual(len(qry), len([x for x in self.names if x.endswith(name)]))

            qry = self.qry.filter(name__iendswith=name)
            self.assertEqual(len(qry), len([x for x in self.names if x.lower().endswith(name.lower())]))

    def test_startswith_lookup_and_istartswith_lookup(self):
        tests = self.names + ['O', 'o', 'ola']
        for name in tests:
            qry = self.qry.filter(name__startswith=name)
            self.assertEqual(len(qry), len([x for x in self.names if x.startswith(name)]))

            qry = self.qry.filter(name__istartswith=name)
            self.assertEqual(len(qry), len([x for x in self.names if x.lower().startswith(name.lower())]))

    def test_regex_lookup_and_iregex_lookup(self):
        tests = ['([A-Z])\w+', '([A-Z])\w+\s[+]\s([A-Z])\w+', '\-Test\-']
        for pattern in tests:
            qry = self.qry.filter(name__regex=pattern)
            self.assertEqual(len(qry), len([x for x in self.names if re.search(pattern, x)]))

            qry = self.qry.filter(name__iregex=pattern)
            self.assertEqual(len(qry), len([x for x in self.names if re.search(pattern, x, flags=re.I)]))

            # Check that the same works for ListField and SetField too
            qry = self.qry.filter(sample_list__item__regex=pattern)
            expected = [
                sample_list for sample_list in self.lists
                if any([bool(re.search(pattern, x)) for x in sample_list])
            ]
            self.assertEqual(len(qry), len(expected))

            qry = self.qry.filter(sample_list__item__iregex=pattern)
            expected = [
                sample_list for sample_list in self.lists
                if any([bool(re.search(pattern, x, flags=re.I)) for x in sample_list])
            ]
            self.assertEqual(len(qry), len(expected))

    def test_item_contains_item_icontains_lookup(self):
        tests = ['O', 'la', 'ola']
        for text in tests:
            qry = self.qry.filter(sample_list__item__contains=text)
            self.assertEqual(len(qry), 1)

            qry = self.qry.filter(sample_list__item__icontains=text)
            self.assertEqual(len(qry), 1)

    def test_item_startswith_item_istartswith_lookup(self):
        tests = ['O', 'ola', 'Ola']
        for text in tests:
            qry = self.qry.filter(sample_list__item__startswith=text)
            self.assertEqual(len(qry), 1)

            qry = self.qry.filter(sample_list__item__istartswith=text)
            self.assertEqual(len(qry), 1)

    def test_item_endswith_item_iendswith_lookup(self):
        tests = ['a', 'la', 'Ola']
        for text in tests:
            qry = self.qry.filter(sample_list__item__endswith=text)
            self.assertEqual(len(qry), 1)

            qry = self.qry.filter(sample_list__item__iendswith=text)
            self.assertEqual(len(qry), 1)


class SliceModel(models.Model):
    field1 = models.CharField(max_length=32)


class SlicingTests(TestCase):

    def test_big_slice(self):
        SliceModel.objects.create(field1="test")
        SliceModel.objects.create(field1="test2")

        self.assertFalse(
            SliceModel.objects.filter(field1__in=["test", "test2"])[9999:]
        )

        self.assertFalse(
            SliceModel.objects.filter(field1__in=["test", "test2"])[9999:10000]
        )

    def test_slicing_multi_query(self):
        SliceModel.objects.create(field1="test")
        SliceModel.objects.create(field1="test2")

        self.assertEqual(
            1,
            len(SliceModel.objects.filter(field1__in=["test", "test2"])[1:])
        )

        self.assertEqual(
            1,
            len(SliceModel.objects.filter(field1__in=["test", "test2"])[:1])
        )

        self.assertEqual(
            2,
            len(SliceModel.objects.filter(field1__in=["test", "test2"])[:2])
        )

        self.assertEqual(
            0,
            len(SliceModel.objects.filter(field1__in=["test", "test2"])[2:])
        )

    def test_slice_params_are_passed_to_query(self):
        for i in range(15):
            SliceModel.objects.create(field1=str(i))

        with sleuth.watch('djangae.db.backends.appengine.rpc.Query.Run') as Run:
            qs = SliceModel.objects.order_by("field1")[:5]

            self.assertEqual(5, len(list(qs)))
            self.assertEqual(Run.calls[0].kwargs['limit'], 5)
            self.assertEqual(Run.calls[0].kwargs['offset'], 0)

            qs = SliceModel.objects.order_by("field1")[5:]
            self.assertEqual(10, len(list(qs)))
            self.assertEqual(Run.calls[1].kwargs['limit'], None)
            self.assertEqual(Run.calls[1].kwargs['offset'], 5)

            qs = SliceModel.objects.order_by("field1")[5:10]
            self.assertEqual(5, len(list(qs)))
            self.assertEqual(Run.calls[2].kwargs['limit'], 5)
            self.assertEqual(Run.calls[2].kwargs['offset'], 5)


class NamespaceTests(TestCase):
    multi_db = True

    @skipIf("ns1" not in settings.DATABASES, "This test is designed for the Djangae testapp settings")
    def test_database_specific_namespaces(self):
        TestFruit.objects.create(name="Apple", color="Red")
        TestFruit.objects.create(name="Orange", color="Orange")

        TestFruit.objects.using("ns1").create(name="Apple", color="Red")

        self.assertEqual(1, TestFruit.objects.using("ns1").count())
        self.assertEqual(2, TestFruit.objects.count())

        with self.assertRaises(TestFruit.DoesNotExist):
            TestFruit.objects.using("ns1").get(name="Orange")

        try:
            TestFruit.objects.get(name="Orange")
        except TestFruit.DoesNotExist:
            self.fail("Unable to retrieve fruit from the default namespace")

        self.assertEqual(1, TestFruit.objects.filter(name="Orange", color="Orange").count())
        self.assertEqual(0, TestFruit.objects.using("ns1").filter(name="Orange", color="Orange").count())

    def test_no_database_namespace_defaults_to_empty(self):
        """
            Test that creating an object without a namespace makes one that is
            retrievable with just a kind and ID
        """

        TestFruit.objects.using("nonamespace").create(name="Apple", color="Red")
        key = rpc.Key.from_path(TestFruit._meta.db_table, "Apple")
        self.assertTrue(rpc.Get([key])[0])

    @skipIf("nonamespace" not in settings.DATABASES, "This test is designed for the Djangae testapp settings")
    def test_move_objects_between_namespaces(self):
        objs = [
            TestFruit.objects.create(name="Banana", color="Black"),
            TestFruit.objects.create(name="Tomato", color="Red"),
        ]
        # First, check that these objects do not exist in the other namespace.
        # We check this in several ways to check that the namespace functionality works in the
        # various different commands of the DB backend
        other_qs = TestFruit.objects.using("nonamespace")
        self.assertEqual(len(other_qs.all()), 0)
        self.assertEqual(other_qs.count(), 0)
        for obj in objs:
            self.assertRaises(TestFruit.DoesNotExist, other_qs.get, name=obj.name)
        # Now re-save both of the objects into the other namespace
        for obj in objs:
            obj.save(using="nonamespace")
        # And now check that they DO exist in that namespace
        self.assertEqual(len(other_qs.all()), 2)
        self.assertEqual(other_qs.count(), 2)
        for obj in objs:
            self.assertEqual(other_qs.get(name=obj.name), obj)
        # Now delete the objects from the original (default) namespace
        TestFruit.objects.all().delete()
        # And now make sure that they exist ONLY in the other namespace
        self.assertEqual(len(TestFruit.objects.all()), 0)
        self.assertEqual(len(other_qs.all()), 2)
        self.assertEqual(TestFruit.objects.count(), 0)
        self.assertEqual(other_qs.count(), 2)
        for obj in objs:
            self.assertRaises(TestFruit.DoesNotExist, TestFruit.objects.get, name=obj.name)
            self.assertEqual(other_qs.get(name=obj.name), obj)


def deferred_func():
    pass


class TestHelperTests(TestCase):
    def test_inconsistent_db(self):
        with inconsistent_db():
            fruit = TestFruit.objects.create(name="banana")
            self.assertEqual(0, TestFruit.objects.count()) # Inconsistent query
            self.assertEqual(1, TestFruit.objects.filter(pk=fruit.pk).count()) # Consistent query

    def test_processing_tasks(self):
        from google.appengine.api import apiproxy_stub_map
        stub = apiproxy_stub_map.apiproxy.GetStub("taskqueue")
        stub._queues[None]._ConstructQueue("another") # Add a test queue
        stub._queues[None]._queue_yaml_parser = None # Make it so that the taskqueue stub doesn't reload from YAML

        self.assertNumTasksEquals(0) # No tasks

        deferred.defer(deferred_func)

        self.assertNumTasksEquals(1, queue_name='default')

        deferred.defer(deferred_func, _queue='another')

        self.assertNumTasksEquals(1, queue_name='another')

        taskqueue.add(url='/')
        self.assertNumTasksEquals(2, queue_name='default')

        self.process_task_queues()

        self.assertNumTasksEquals(0) # No tasks


class Zoo(models.Model):
    pass


class Enclosure(models.Model):
    zoo = models.ForeignKey(Zoo)


class Animal(models.Model):
    enclosure = models.ForeignKey(Enclosure)


class CascadeDeletionTests(TestCase):
    def test_deleting_more_than_30_items(self):
        zoo = Zoo.objects.create()

        for i in range(40):
            enclosure = Enclosure.objects.create(zoo=zoo)
            for i in range(2):
                Animal.objects.create(enclosure=enclosure)

        self.assertEqual(Animal.objects.count(), 80)

        zoo.delete()

        self.assertEqual(Enclosure.objects.count(), 0)
        self.assertEqual(Animal.objects.count(), 0)


class AsyncMultiQueryTests(TestCase):

    def test_offset_is_correctly_applied(self):
        TestUser.objects.create(username="Adam", field2="Adam")
        u2 = TestUser.objects.create(username="Bob")
        TestUser.objects.create(username="Chloe")

        qs = TestUser.objects.filter(
            Q(field2="Adam") | Q(username__in=["Adam", "Bob"])
        ).order_by("username")[1:]

        self.assertEqual(len(qs), 1)
        self.assertItemsEqual([u2], qs)

    def test_limit_is_correctly_applied(self):
        TestUser.objects.create(username="Adam", field2="Adam")
        u2 = TestUser.objects.create(username="Bob")
        TestUser.objects.create(username="Chloe")

        qs = TestUser.objects.filter(
            Q(field2="Adam") | Q(username__in=["Adam", "Bob", "Chloe"])
        ).order_by("username")[1:2]

        self.assertEqual(len(qs), 1)
        self.assertItemsEqual([u2], qs)


class UUIDTestModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)


class FieldConversionTests(TestCase):
    def test_uuid_field_handled(self):
        instance = UUIDTestModel.objects.create()
        self.assertTrue(isinstance(instance.uuid, uuid.UUID))

        instance.refresh_from_db()
        self.assertTrue(isinstance(instance.uuid, uuid.UUID))
