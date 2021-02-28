import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ConfirmationCode(models.Model):

    email = models.EmailField(
        max_length=30, unique=True,
        verbose_name='email')

    confirmation_code = models.CharField(
        max_length=30,
        verbose_name='confirmation code')

    last_sent = models.DateTimeField(
        auto_now=True,
        verbose_name='last sent confirmation code datetime')

    confirmed = models.BooleanField(
        default=False,
        verbose_name='is user confirmed')


class User(AbstractUser):

    class RoleChoices(models.TextChoices):
        USER = 'USR',
        MODERATOR = 'MOD',
        ADMIN = 'ADM',

    bio = models.TextField(
        max_length=500, blank=True,
        verbose_name='bio description')

    role = models.TextField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.USER,
        verbose_name='user role')

    email = models.EmailField(
        max_length=35,
        blank=False,
        null=False,
        unique=True,
        verbose_name='user email')

    @property
    def is_moderator(self):
        return self.role == self.RoleChoices.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.RoleChoices.ADMIN or self.is_staff


class Category(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='category title')

    slug = models.SlugField(
        unique=True,
        verbose_name='slug')

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='genre title')

    slug = models.SlugField(
        unique=True,
        verbose_name='slug')

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='title name')

    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(datetime.datetime.now().year)],
        help_text='Use the following format: <YYYY>',
        verbose_name='title year')

    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)],
        null=True,
        verbose_name='title rating')

    description = models.TextField(
        verbose_name='title description')

    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='title genre')

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='title category')

    def __str__(self):
        return self.name


class Review(models.Model):

    text = models.TextField(
        verbose_name='review text')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review',
        verbose_name='review author')

    score = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)],
        null=True,
        verbose_name='review rationg scores from 0 to 10')

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publication date')

    title = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        null=True,
        related_name='review',
        verbose_name='reviewed title')

    def __str__(self):
        return self.text


class Comment(models.Model):

    text = models.TextField(
        verbose_name='comment text')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='comment author')

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='comment publication date')

    review = models.ForeignKey(
        Review,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comments',
        verbose_name='commented review')

    def __str__(self):
        return self.text
