from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'cover_photo']

    def validate_cover_photo(self, value):
        if value and not value.name.lower().endswith(('.png', '.jpg')):
            raise serializers.ValidationError("The file must be an image in PNG or JPG format")
        return value
