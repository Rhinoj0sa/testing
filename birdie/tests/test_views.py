import pytest

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from mixer.backend.django import mixer

from ..views import HomeView, AdminView, PostUpdateView

pytestmark = pytest.mark.django


@pytest.mark.django_db
class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        response = HomeView.as_view()(req)
        assert response.status_code == 200


@pytest.mark.django_db
class TestAdminView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        response = AdminView.as_view()(req)
        assert 'login' in response.url

    def test_superuser(self):
        user = mixer.blend('auth.User', is_superUser=True)
        req = RequestFactory().get('/')
        req.user = user
        response = AdminView.as_view()(req)
        assert response.status_code == 200, 'Authenticated'


@pytest.mark.django_db
class TestPostUpdateView:
    def test_get(self):
        req = RequestFactory().get('/')
        obj = mixer.blend("birdie.Post")
        response = PostUpdateView.as_view()(req, pk=obj.pk)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_post(self):
        post = mixer.blend("birdie.Post")
        data = {'body': 'new body test data'}
        req = RequestFactory().post('/', data=data)
        response = PostUpdateView.as_view()(req, pk=post.pk)
        assert response.status_code == 302, 'should redirect to success view'
        post.refresh_from_db()
        assert post.body == 'new body test data', 'should update the post'
