import requests
from datetime import datetime
from anime.models import Anime
from anime.scripts.episode_summary import episode_summary_getter
from anime.scripts.studio import get_studio
from anime.scripts.directors import get_directors
from anime.scripts.genre import genre_adder
from anime.scripts.characters import character_adder


# For adding anime one by one, referencing their ID as it appears in Kitsu's database
def add(i):

    base_url = 'https://kitsu.io/api/edge/'
    anime_url = f'anime/{i}'

    response = requests.get(f"{base_url}{anime_url}")

    # skipping the anime in case of server errors
    if response.status_code == 200 and response.json()['data'] != []:

        id = response.json()['data']['id']

        # getting the English and Japanese names, and setting them to be the same in case there is no Japanese name provided
        name_en = str(response.json()['data']
                      ['attributes']['titles'].get('en'))
        name_jp = str(response.json()['data']
                      ['attributes']['titles'].get('en_jp'))
        if name_en == 'None':
            name_en = name_jp

        print(f'   >>> Working on the anime {name_en}')

        # getting slug and description without any checks as these are present for all anime
        slug = str(response.json()['data']['attributes'].get('slug'))
        about = str(response.json()['data']['attributes'].get('synopsis'))
        age_rating = response.json()['data']['attributes'].get(
            'ageRating')

        # checking if the anime is finished, then fetching the date it ended
        if response.json()['data']['attributes']['status'] == 'finished':
            started = datetime.strptime(
                response.json()['data']['attributes']['startDate'], '%Y-%m-%d').date()
            ended = datetime.strptime(
                response.json()['data']['attributes']['endDate'], '%Y-%m-%d').date()
            is_completed = True

            # if it's a series, then fetching the number of episodes, otherwise setting equal to one for movies and OVAs/ONAs
            if response.json()['data']['attributes']['subtype'] in ('TV', 'tv'):
                num_of_eps = response.json(
                )['data']['attributes']['episodeCount']
            else:
                num_of_eps = 1
        # not trying to get the finishing date in case it's ongoing, but because the database accepts only a date object, assigning 11-11-1111
        elif response.json()['data']['attributes']['status'] == 'current':
            started = datetime.strptime(
                response.json()['data']['attributes']['startDate'], '%Y-%m-%d').date()
            ended = datetime(1111, 11, 11).date()
            is_completed = False
            num_of_eps = 0

        # if the anime hasn't even started airing yet, then setting 11-11-1111 for both start and end dates
        elif response.json()['data']['attributes']['status'] in ('tba', 'upcoming', 'unreleased'):
            started = ended = datetime(1111, 11, 11).date()
            is_completed = False
            num_of_eps = 0

        # getting the ratings and type as these are always there
        popularity_rank = response.json()['data']['attributes'].get(
            'popularityRank')
        rating = response.json()['data']['attributes'].get('averageRating')
        type = "{} ({})".format(str(response.json()[
            'data'].get('type')).title(), str(response.json()['data']['attributes'].get('subtype')).upper())

        # trying to get the poster and cover image, setting to empty string if not available
        try:
            poster_image = str(
                response.json()['data']['attributes']['posterImage'].get('original'))
        except:
            poster_image = ''
        try:
            cover_image = str(
                response.json()['data']['attributes']['coverImage'].get('original'))
        except:
            cover_image = ''

        studio = get_studio(response)
        episode_summary = episode_summary_getter(id)
        directors = get_directors(response)

        # creating the object using the Django object manager
        anime = Anime.objects.create(
            name_en=name_en, name_jp=name_jp, slug=slug, about=about, started=started, ended=ended, is_completed=is_completed,
            studio=studio, cover_image=cover_image, poster_image=poster_image, type=type, rating=rating, num_of_eps=num_of_eps, directors=directors, episode_summary=episode_summary, popularity_rank=popularity_rank, age_rating=age_rating
        )
        anime.save()

        # printing a little confirmation message if everything goes fine
        print(
            f'\n    >> {type}: {name_en} ({name_jp}) added to the database successfully ^w^\n')

        genre_adder(anime, response)

        character_adder(anime, id)

        print(
            f'\n    >> Added all characters to the anime: {anime.name_en} ＾▽＾')

        print(
            f'\n    >>> Added the anime {anime.name_en} and it\'s related genres and characters successfully! ＼(~o~)／ \n')

        print('\n-----------------------------------------------------------------------------------------------------\n')

    # in case the details of the anime could not be fetched
    else:
        print(' >> The server responded with a status code of {}\n'.format(
            response.status_code))
        print('\n-----------------------------------------------------------------------------------------------------\n')
