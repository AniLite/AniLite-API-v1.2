from django.urls import path
from .views import *

urlpatterns = [

    # anime related urls

    path('anime/', AnimeListView.as_view(), name='anime-list'),
    path('anime/create', AnimeCreateView.as_view(), name='anime-create'),
    path('anime/<str:slug>', AnimeDetailView.as_view(), name='anime-detail'),
    path('anime/<str:slug>/update', AnimeUpdateView.as_view(), name='anime-update'),
    path('anime/<str:slug>/delete', AnimeDeleteView.as_view(), name='anime-delete'),

    # genre related urls

    path('genre/', GenreListView.as_view(), name='genre-list'),
    path('genre/create', GenreCreateView.as_view(), name='genre-create'),
    path('genre/<str:slug>', GenreDetailView.as_view(), name='genre-detail'),
    path('genre/<str:slug>/update', GenreUpdateView.as_view(), name='genre-update'),
    path('genre/<str:slug>/delete', GenreDeleteView.as_view(), name='genre-delete'),

    # character related urls

    path('character/', CharacterListView.as_view(), name='character-list'),
    path('character/create', CharacterCreateView.as_view(), name='character-create'),
    path('character/<str:slug>', CharacterDetailView.as_view(),
         name='character-detail'),
    path('character/<str:slug>/update',
         CharacterUpdateView.as_view(), name='character-update'),
    path('character/<str:slug>/delete',
         CharacterDeleteView.as_view(), name='character-delete'),
]
