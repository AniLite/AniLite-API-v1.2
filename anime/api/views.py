from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import AnimeDetailSerializer, AnimeListSerializer, CharacterDetailSerializer, CharacterListSerializer,  GenreSerializer
from anime.models import Anime, Genre, Character
from .mixins import MultipleFieldLookupMixin

########################## USING GENERIC VIEWS ##########################


##### Anime related views #####


class AnimeListView(ListAPIView):

    def get_queryset(self):

        queryset = Anime.objects.all()
        fields = ['startswith', 'includes', 'sort', 'genre', 'type']

        for field in fields:

            globals()[field] = self.request.query_params.get(f'{field}')

            if globals()[field]:

                if field == 'includes':
                    queryset = queryset.filter(
                        name_en__icontains=globals()[field])
                    if queryset == Anime.objects.all():
                        queryset = queryset.filter(
                            name_jp__icontains=globals()[field])

                elif field == 'genre':
                    genres = globals()[field].split(' ')
                    for count, genre in enumerate(genres, 1):
                        globals()['qs' + str(count)
                                  ] = Genre.objects.get(slug__iexact=genre).animes.all()
                        queryset = queryset.intersection(
                            globals()['qs' + str(count)])

                elif field == 'startswith':
                    queryset = queryset.filter(
                        name_en__istartswith=globals()[field])

                elif field == 'type':
                    if globals()[field] == 'movie':
                        queryset = queryset.filter(type__icontains='MOVIE')

                elif field == 'sort':
                    if globals()[field] == 'rating':
                        queryset = queryset.order_by(
                            '-' + str(globals()[field]))
                    else:
                        queryset = queryset.order_by(str(globals()[field]))

        return queryset

    serializer_class = AnimeListSerializer


class AnimeDetailView(MultipleFieldLookupMixin, RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailSerializer
    lookup_fields = ['slug']


class AnimeCreateView(CreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeListSerializer


class AnimeUpdateView(MultipleFieldLookupMixin, UpdateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeListSerializer
    lookup_fields = ['slug']


class AnimeDeleteView(MultipleFieldLookupMixin, DestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeListSerializer
    lookup_fields = ['slug']


##### Genre related views #####


class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailView(MultipleFieldLookupMixin, RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_fields = ['slug']


class GenreCreateView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreUpdateView(MultipleFieldLookupMixin, UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_fields = ['slug']


class GenreDeleteView(MultipleFieldLookupMixin, DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_fields = ['slug']


##### Character related views #####


class CharacterListView(ListAPIView):

    def get_queryset(self):

        queryset = Character.objects.all()
        fields = ['startswith', 'includes', 'sort']

        for field in fields:

            globals()[field] = self.request.query_params.get(f'{field}')

            if globals()[field]:

                if field == 'startswith':
                    queryset = queryset.filter(
                        name__istartswith=globals()[field])

                elif field == 'includes':
                    queryset = queryset.filter(
                        name__icontains=globals()[field])

                elif field == 'sort':
                    queryset = queryset.order_by(str(globals()[field]))

        return queryset

    serializer_class = CharacterListSerializer


class CharacterDetailView(MultipleFieldLookupMixin, RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    lookup_fields = ['slug']


class CharacterCreateView(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer


class CharacterUpdateView(MultipleFieldLookupMixin, UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    lookup_fields = ['slug']


class CharacterDeleteView(MultipleFieldLookupMixin, DestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    lookup_fields = ['slug']


########################## USING API VIEWS ##########################


# from rest_framework.response import Response
# from rest_framework.decorators import api_view


# @api_view(['GET'])
# def list_anime(request):
#     queryset = Anime.objects.all()
#     serializer = AnimeListSerializer(queryset, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def anime_detail(request, slug):
#     queryset = Anime.objects.get(slug__iexact=slug)
#     serializer = AnimeDetailSerializer(queryset, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def list_genre(request):
#     queryset = Genre.objects.all()
#     serializer = GenreSerializer(queryset, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def genre_detail(request, slug):
#     queryset = Genre.objects.get(slug__iexact=slug)
#     serializer = GenreSerializer(queryset, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def list_character(request):
#     queryset = Character.objects.all()
#     serializer = CharacterListSerializer(queryset, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def character_detail(request, slug):
#     queryset = Character.objects.get(slug__iexact=slug)
#     serializer = CharacterDetailSerializer(queryset, many=False)
#     return Response(serializer.data)
