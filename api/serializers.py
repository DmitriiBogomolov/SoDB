from rest_framework import exceptions, serializers

from .models import (Category, Comment, ConfirmationCode, Genre, Review, Title,
                     User)


class ConfirmationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'email', 'confirmation_code', 'last_sent')
        model = ConfirmationCode
        read_only_fields = ('last_sent', 'confirmation_code')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name',
                  'username', 'bio', 'email', 'role')
        model = User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class GenreRelatedField(serializers.RelatedField):

    def to_representation(self, obj):
        data = {
            'name': obj.name,
            'slug': obj.slug
        }
        return data

    def to_internal_value(self, slug):
        return Genre.objects.get(slug=slug)


class CategoryRelatedField(serializers.RelatedField):

    def to_representation(self, obj):
        data = {
            'name': obj.name,
            'slug': obj.slug
        }
        return data

    def to_internal_value(self, slug):
        return Category.objects.get(slug=slug)


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreRelatedField(
        queryset=Genre.objects.all(), many=True)
    category = CategoryRelatedField(
        queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    def create(self, validated_data):
        title = validated_data['title']
        user = validated_data['author']
        if Review.objects.filter(author=user, title=title).exists():
            raise exceptions.ValidationError('Вы уже оставили отзыв')
        return Review(**validated_data)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
