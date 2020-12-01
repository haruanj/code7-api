from rest_framework import viewsets
from news.serializers import NewsInputSerializer, NewsOutputSerializer, AuthorSerializer
from news.services.author import list_authors
from news.services.news import search_news, get_news, NewsDoesNotExistException
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


class NewsViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = NewsOutputSerializer(search_news(query=request.GET.get("q", "")), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NewsInputSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            news = serializer.save()
            return Response(NewsOutputSerializer(news).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            news = get_news(pk)
        except NewsDoesNotExistException:
            raise NotFound(detail="News not found", code=404)

        serializer = NewsInputSerializer(news, data=request.data)
        if serializer.is_valid(raise_exception=True):
            news = serializer.save()
            return Response(NewsOutputSerializer(news).data)

    def retrieve(self, request, pk=None):
        serializer = NewsOutputSerializer(get_news(pk))
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            news = get_news(pk)
            news.delete()
        except NewsDoesNotExistException:
            pass
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class AuthorViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = AuthorSerializer(list_authors(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
