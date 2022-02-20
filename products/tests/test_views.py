from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from mixer.backend.django import mixer
import pytest

from products.views import product_detail


@pytest.mark.django_db
class TestViews:
    def test_product_detail_authenticated(self):
        path = reverse('detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        print(request)
        response = product_detail(request, pk=1)
        print(f"response: {response}")
        assert response.status_code == 404
