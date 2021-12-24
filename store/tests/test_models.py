from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='Django', slug='django')

    def test_category_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Django')

class TestProductModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='Django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='11.99', image='djnago')

    def test_product_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

