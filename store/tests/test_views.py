from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from store.models import Category, Product
from store.views import product_list


class TestViewResponses(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='Django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='11.99', image='djnago')

    def test_url_allowed_hosts(self):
        '''
        Test allowed hosts
        :return:
        '''
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        '''
        Test Product response status
        :return:
        '''
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        '''
        Test Category response status
        :return:
        '''
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = product_list(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>', html)
        self.assertTrue(html.startswith('<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('book/django-beginners')
        response = product_list(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>', html)
        self.assertTrue(html.startswith('<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

