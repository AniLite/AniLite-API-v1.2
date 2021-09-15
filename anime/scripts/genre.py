import requests
from anime.models import Genre


# function to first make a list of all the genres of the anime, and then fetch these Genre objects from the database and bind them to the Anime object under consideration
def genre_adder(anime, response):
    link_to_genres = response.json(
    )['data']['relationships']['genres']['links']['related']
    res = requests.get(link_to_genres)
    slugs = [item['attributes']['slug']
             for item in res.json()['data']]
    genres = [Genre.objects.get(slug__iexact=slug)
              for slug in slugs]
    for genre in genres:
        anime.genres.add(genre)
        print(
            f'> {genre} added to the list of genres for the anime: {anime.name_en}')
    print(
        f'\n    >> Added all genres for the anime {anime.name_en} ^_^\n')
