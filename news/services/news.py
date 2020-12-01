from news.documents import News, Author
from news.services.author import search_author
from mongoengine.queryset.visitor import Q
from mongoengine import DoesNotExist


class NewsDoesNotExistException(Exception):
    pass


def list_news():
    return list(News.objects)


def search_news(query=""):
    if query:
        authors = search_author(query)
        return list(
            News.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query) | Q(author__in=authors)
            ).select_related()
        )
    else:
        return list_news()


def get_news(news_id) -> News:
    try:
        return News.objects(id=news_id).get()
    except DoesNotExist:
        raise NewsDoesNotExistException()


def update_news(news, title: str, description: str, author: Author) -> News:
    news.title = title
    news.description = description
    news.author = author
    news.save()
    return news


def create_news(title: str, description: str, author: Author) -> News:
    news = News(title=title, description=description, author=author)
    news.save()
    return news


def delete_news(news):
    news.delete()
