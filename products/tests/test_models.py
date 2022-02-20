from mixer.backend.django import mixer
import pytest

# from testing.products.models import Product


@pytest.mark.django_db
class TestModels:

    def test_product_is_in_stock(self):
        product = mixer.blend('products.Product', quantity=1)
        print(product.__dict__)
        print(f"stock: {product.is_in_stock()}")
        assert product.is_in_stock() == True

    def test_product_is_not_in_stock(self):
        product = mixer.blend('products.Product', quantity=0)
        print(product.__dict__)
        print(f"stock: {product.is_in_stock()}")
        assert product.is_in_stock() == False
