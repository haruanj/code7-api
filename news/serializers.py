from rest_framework import serializers
from news.services.author import create_author, get_author
from news.services.news import create_news, update_news


class AuthorSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)

    def create(self, validated_data):
        return create_author(**validated_data)


class BaseNewsSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)


class NewsOutputSerializer(BaseNewsSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return AuthorSerializer(obj.author).data


class NewsInputSerializer(BaseNewsSerializer):
    author = serializers.CharField(write_only=True)

    def validate_author(self, value):
        author = get_author(value)
        if not author:
            raise serializers.ValidationError("Invalid author")
        return author

    def create(self, validated_data):
        return create_news(**validated_data)

    def update(self, instance, validated_data):
        return update_news(instance, **validated_data)
