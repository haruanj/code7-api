from django.contrib import admin
from rest_framework import routers
from news.views import NewsViewSet, AuthorViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"news", NewsViewSet, basename="news")
router.register(r"authors", AuthorViewSet, basename="authors")

urlpatterns = [
    path("", include(router.urls)),
]
