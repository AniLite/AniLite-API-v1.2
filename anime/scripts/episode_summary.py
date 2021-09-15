import requests


def episode_summary_getter(id):

    def add_summary(link, data=''):

        response = requests.get(link)

        for item in response.json()['data']:

            summary = item['attributes'].get('synopsis')
            title = item['attributes'].get('canonicalTitle')
            air_date = item['attributes'].get('airdate')

            try:
                thumbnail = item['attributes']['thumbnail'].get('original')
            except:
                thumbnail = ''

            if data == '':
                data = []

            data.append([{'Summary': summary, 'Title': title,
                          'Air Date': air_date, 'Thumbnail': thumbnail}])

        if 'next' in response.json()['links']:
            add_summary(response.json()['links']['next'], data)
        return data

    episodes_url = f'https://kitsu.io/api/edge/anime/{id}/episodes?page%5Blimit%5D=20'

    data = add_summary(episodes_url)
    return data
