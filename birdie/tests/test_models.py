import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django


@pytest.mark.django_db
class TestPost:
    def test_model(self):
        obj = mixer.blend("birdie.Post")
        print(f"this is the post{obj.__dict__}")
        assert obj.pk == 1, 'should have an instance there is no fucking db'
