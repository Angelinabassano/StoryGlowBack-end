from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'cover_photo']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("The title must be at least 5 characters")
        if len(value) > 120:
            raise serializers.ValidationError("The title should not exceed 120 characters")
        if not re.match(r'^[A-Za-z0-9\s]+$', value):
            raise serializers.ValidationError("The title can only contain letters, numbers and spaces")
        return value

    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("The description must be at least 20 characters")
        return value

    def validate_cover_photo(self, value):
        if value and not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("The file must be an image in PNG, JPG or JPEG format")
        return value