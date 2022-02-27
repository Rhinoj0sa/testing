import pytest

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from mixer.backend.django import mixer

from .. import views

pytestmark = pytest.mark.django


@pytest.mark.django_db
class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        response = views.HomeView.as_view()(req)
        assert response.status_code == 200


@pytest.mark.django_db
class TestAdminView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        response = views.AdminView.as_view()(req)
        assert 'login' in response.url

    def test_superuser(self):
        user = mixer.blend('auth.User', is_superUser=True)
        req = RequestFactory().get('/')
        req.user = user
        response = views.AdminView.as_view()(req)
        assert response.status_code == 200, 'Authenticated'
