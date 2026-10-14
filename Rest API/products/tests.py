from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductAPITests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'Wireless Mouse',
            'description': 'Ergonomic optical mouse',
            'price': '25.99',
            'stock_quantity': 50,
            'category': 'Electronics'
        }
        self.invalid_payload = {
            'name': 'Cheap Pen',
            'description': 'Blue ballpoint pen',
            'price': '0.00',
            'stock_quantity': 100,
            'category': 'Stationery'
        }
        self.product = Product.objects.create(
            name='Keyboard',
            description='Mechanical gaming keyboard',
            price='75.50',
            stock_quantity=20,
            category='Electronics'
        )
        self.list_url = reverse('product-list')
        self.detail_url = reverse('product-detail', args=[self.product.id])

    def test_create_product(self):
        response = self.client.post(self.list_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(response.data['name'], 'Wireless Mouse')

    def test_get_product_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Keyboard')

    def test_update_product(self):
        updated_payload = {
            'name': 'RGB Mechanical Keyboard',
            'description': 'Updated description',
            'price': '89.99',
            'stock_quantity': 15,
            'category': 'Electronics'
        }
        response = self.client.put(self.detail_url, updated_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'RGB Mechanical Keyboard')
        self.assertEqual(str(self.product.price), '89.99')

    def test_delete_product(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_invalid_price_zero(self):
        response = self.client.post(self.list_url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_price_negative(self):
        payload = {
            'name': 'Faulty Item',
            'description': 'Negative price item',
            'price': '-5.00',
            'stock_quantity': 10,
            'category': 'General'
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
