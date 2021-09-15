from rest_framework import serializers
from anime.models import Anime, Genre, Character

site_url = 'https://anilite-api.herokuapp.com'


class AnimeListSerializer(serializers.ModelSerializer):

    genres = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Anime
        fields = ['id', 'type', 'name_en', 'name_jp', 'slug',
                  'about', 'started', 'is_completed', 'ended', 'rating', 'num_of_eps', 'poster_image', 'cover_image', 'studio', 'genres']

    def get_genres(self, obj):
        data = [
            {
                'id': genre.id,
                'name': genre.name,
                'link': f'{site_url}/genre/{genre.slug}'
            }
            for genre in obj.genres.all()
        ]
        return data


class AnimeDetailSerializer(serializers.ModelSerializer):

    genres = serializers.SerializerMethodField(read_only=True)
    characters = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Anime
        fields = ['id', 'type', 'name_en', 'name_jp', 'slug',
                  'about', 'age_rating', 'started', 'is_completed', 'ended', 'rating', 'popularity_rank', 'num_of_eps', 'poster_image', 'cover_image', 'studio', 'directors', 'genres', 'characters', 'episode_summary']

    def get_genres(self, obj):
        data = [
            {
                'id': genre.id,
                'name': genre.name,
                'link': f'{site_url}/genre/{genre.slug}'
            }
            for genre in obj.genres.all()
        ]
        return data

    def get_characters(self, obj):
        data = [
            {
                'id': character.id,
                'name': character.name,
                'image': character.image,
                'link': f'{site_url}/character/{character.slug}'
            }
            for character in obj.characters.all()
        ]
        return data


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']


class CharacterListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ['id', 'name', 'slug', 'image']


class CharacterDetailSerializer(serializers.ModelSerializer):

    anime = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'slug', 'about', 'image', 'voice_en', 'voice_jp',
                  'other_names', 'anime']

    def get_anime(self, obj):
        data = [
            {
                'name': anime.name_en,
                'link': f'{site_url}/anime/{anime.slug}'
            }
            for anime in obj.anime.all()
        ]
        return data
