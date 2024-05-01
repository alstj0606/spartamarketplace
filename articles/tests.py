from django.test import TestCase
from django.urls import reverse
from .models import Article
from .views import ArticleListAPIView, ArticleDetailAPIView

class ArticleTestCase(TestCase):
    def setUp(self):
        self.article = Article.objects.create(title='Test Article', content='Test Content')

    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')
