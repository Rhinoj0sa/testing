import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django


@pytest.mark.django_db
class TestPost:
    def test_model(self):
        obj = mixer.blend("birdie.Post")
        print(f"this is the post{obj.__dict__}")
        assert obj.pk == 1, 'should have an instance with pk 1'

    def test_get_excerpt(self):
        obj = mixer.blend("birdie.Post")
        print(f"this is the post{obj.__dict__}")
        i = 5
        result = obj.get_excerpt(i)
        print(f"result of the first {i}is: {result}")
        assert result == obj.body[:i], "expected the first 5 chars of the post in this case Hello"
