import requests


# fetching the names of directors
def get_directors(response):
    lst_directors = []
    link = response.json(
    )['data']['relationships']['staff']['links'].get('related')
    res = requests.get(link + '?page%5Blimit%5D=20')
    if res.status_code == 200 and res.json()['data'] != []:
        for item in res.json()['data']:
            roles = item['attributes']['role'].split(',')
            if 'Director' in roles:
                link_one = item['relationships']['person']['links']['related']
                r = requests.get(link_one)
                lst_directors.insert(0, r.json(
                )['data']['attributes'].get('name'))
        return ', '.join([str(director) for director in lst_directors])
