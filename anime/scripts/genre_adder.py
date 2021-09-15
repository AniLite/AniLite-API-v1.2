import requests
from anime.models import Genre


def add():
    base_url = 'https://kitsu.io/api/edge/'
    i = 0
    while i < 65:
        i += 1
        genre_url = f'genres/{i}'
        response = requests.get(f'{base_url}{genre_url}')
        if response.status_code == 200 and response.json()['data'] != []:
            name = response.json()['data']['attributes'].get('name')
            slug = response.json()['data']['attributes'].get('slug')
            try:
                genre = Genre.objects.get(slug_iexact=slug)
            except:
                genre = None
            if genre == None:
                Genre.objects.create(name=str(name), slug=str(slug))
                print(f'> Added genre #{i}: {name}!')
