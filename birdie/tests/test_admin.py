import pytest
from mixer.backend.django import mixer
from django.contrib.admin.sites import AdminSite
from .. import models
from .. import admin

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestPostAdmin:
    def test_excerpt(self):
        site = AdminSite()
        post_admin = admin.PostAdmin(models.Post, site)
        obj = mixer.blend("birdie.Post", body='Hello world!')
        print(obj.__dict__)
        result = post_admin.excerpt(obj)
        print(result)
        assert result == 'Hello'
