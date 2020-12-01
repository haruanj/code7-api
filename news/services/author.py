from news.documents import Author


def create_author(name: str) -> Author:
    author = Author(name=name)
    author.save()
    return author


def list_authors():
    return list(Author.objects)


def search_author(name):
    return list(Author.objects(name__icontains=name))


def get_author(author_id) -> Author:
    return Author.objects(id=author_id)[0]
