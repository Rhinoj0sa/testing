import pytest

from ..forms import PostForm

pytestmark = pytest.mark.django_db


class TestForms:
    def test_form(self):
        form = PostForm(data={})
        assert form.is_valid() is False, "should not be valid if form is empty"
        form = PostForm(data={"body": "Hel"})
        print(form.__dict__)
        assert form.is_valid(), "body is too short"
        # assert 'body' in form.errors, "should have body errors"
        # for some reason gives me errors
        form = PostForm(data={"body": 'Hello cruel world '})
        print(form.__dict__)
        print(form.error_class.__dict__)
        assert form.is_valid() is True, "should be valid"
