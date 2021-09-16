import requests
from anime.models import Character


def create_character(slug):
    link = f'https://kitsu.io/api/edge/characters?filter[slug]={slug}'
    response = requests.get(link)
    if response.status_code == 200 and response.json()['data'] != []:

        name = response.json()['data'][0]['attributes']['name']

        try:
            about = response.json()['data'][0]['attributes'].get(
                'description')
        except:
            about = 'Not Available'

        def get_other_names():

            lst_names = response.json(
            )['data'][0]['attributes']['otherNames']
            names = ''
            if lst_names != []:
                for count, name in enumerate(lst_names):
                    if count == 0:
                        names += f'{name}'
                    else:
                        names += f', {name}'
            else:
                names = ''
            return names

        other_names = get_other_names()

        def get_voice_actors():

            link = response.json()[
                'data'][0]['relationships']['castings']['links']['related'] + '?page%5Blimit%5D=20'

            res = requests.get(link)
            names = {}
            for item in res.json()['data']:

                if item['attributes']['voiceActor'] == True:

                    if item['attributes']['language'] == 'Japanese':
                        jp_voice_link = item['relationships']['person']['links']['related']
                        r = requests.get(jp_voice_link)
                        if r.json()['data'] is not None:
                            jp = r.json()[
                                'data']['attributes']['name']
                            if 'jp' not in names:
                                names['jp'] = jp

                    elif item['attributes']['language'] == 'English':
                        en_voice_link = item['relationships']['person']['links']['related']
                        r = requests.get(en_voice_link)
                        if r.json()['data'] is not None:
                            en = r.json()[
                                'data']['attributes']['name']
                            if 'en' not in names:
                                names['en'] = en

            return names

        names = get_voice_actors()
        voice_en, voice_jp = names.get('en'), names.get('jp')

        try:
            image = response.json()[
                'data'][0]['attributes']['image']['original']
        except:
            image = ''

        character = Character.objects.create(
            name=name, about=about, slug=slug, voice_en=voice_en, voice_jp=voice_jp, other_names=other_names, image=image)

        return character

    else:

        return None


def character_adder(anime, id):

    characters_url = f'https://kitsu.io/api/edge/anime/{id}/characters?page%5Blimit%5D=20'

    def add_characters(link):
        response = requests.get(link)
        for item in response.json()['data']:
            slug_link = f"https://kitsu.io/api/edge/media-characters/{item['id']}/character"
            r = requests.get(slug_link)
            slug = r.json()['data']['attributes']['slug']
            name = r.json()['data']['attributes']['name']
            try:
                character = Character.objects.get(
                    slug__iexact=slug)
                anime.characters.add(character)
                print(
                    f'> Connected character: {name} to anime: {anime.name_en}')
            except:
                char = create_character(slug)
                if char == None:
                    print(
                        f'\n    > Uh oh, something went wrong while fetching the information for character {name} :/ \n')
                else:
                    anime.characters.add(char)
                    print(
                        f'> Character: {name} added to the database and connected to {anime.name_en} successfully!')

        if 'next' in response.json()['links'].keys():
            add_characters(response.json()['links']['next'])
        else:
            return 0

    add_characters(characters_url)
