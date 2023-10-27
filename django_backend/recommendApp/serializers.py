from rest_framework import serializers
from recommendApp.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('bookid', 'title', 'author', 'genre', 'studyarea')