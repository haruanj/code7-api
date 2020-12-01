from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from mongoengine import connect, disconnect
from news.services.news import create_news
from news.services.author import create_author


class TestNewsViewSet(TestCase):
    def test_news_list(self):
        response = self.client.get(reverse("news-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(str(response.content, encoding="utf8"), [])

        author = create_author("author_name")
        news = create_news("new", "new", author)
        response = self.client.get(reverse("news-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            [
                {
                    "id": str(news.id),
                    "title": news.title,
                    "description": news.description,
                    "author": {"id": str(author.id), "name": author.name},
                }
            ],
        )

        response = self.client.get(reverse("news-list"), {"q": "batman"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            [],
        )

        response = self.client.get(reverse("news-list"), {"q": "NEW"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            [
                {
                    "id": str(news.id),
                    "title": news.title,
                    "description": news.description,
                    "author": {"id": str(author.id), "name": author.name},
                }
            ],
        )

        response = self.client.get(reverse("news-list"), {"q": "AUTHOR_NAM"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            [
                {
                    "id": str(news.id),
                    "title": news.title,
                    "description": news.description,
                    "author": {"id": str(author.id), "name": author.name},
                }
            ],
        )
