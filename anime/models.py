from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return (f"Genre: '{self.name.title()}'")

    class Meta:
        ordering = ['name']


class Character(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True, unique=True)
    about = models.TextField(null=True, blank=True)
    voice_en = models.CharField(max_length=100, null=True, blank=True)
    voice_jp = models.CharField(max_length=100, null=True, blank=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    other_names = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.name)

    class Meta:
        ordering = ['name']


class Anime(models.Model):

    name_en = models.CharField(max_length=150, null=True, blank=True)
    name_jp = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    age_rating = models.CharField(max_length=20, blank=True, null=True)
    started = models.DateField(null=True, blank=True)
    ended = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name='animes')
    characters = models.ManyToManyField(
        Character, blank=True, related_name='anime')
    num_of_eps = models.IntegerField(null=True, blank=True)
    is_completed = models.BooleanField(null=True, blank=True)
    studio = models.CharField(max_length=150, null=True, blank=True)
    directors = models.CharField(max_length=150, null=True, blank=True)
    rating = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=4)
    popularity_rank = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    episode_summary = models.JSONField(null=True, blank=True)
    poster_image = models.URLField(max_length=255, null=True, blank=True)
    cover_image = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.type} - {self.name_en} ({self.name_jp})'

    class Meta:
        ordering = ['name_en']
