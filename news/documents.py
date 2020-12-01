import mongoengine
from mongoengine import Document, StringField, ReferenceField


class Author(Document):
    name = StringField(required=True, max_lenght=255)


class News(Document):
    title = StringField(required=True, max_lenght=255)
    description = StringField(required=True)
    author = ReferenceField("Author", required=True, reverse_delete_rule=mongoengine.DO_NOTHING)
