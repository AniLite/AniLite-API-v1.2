import requests


# fetching the name of the studio, setting to 'Not Available' if that's the case
def get_studio(response):
    link_one = response.json(
    )['data']['relationships']['animeProductions']['links'].get('related')
    res = requests.get(link_one + '?page%5Blimit%5D=20')
    if res.status_code == 200 and res.json()['data'] != []:
        for item in res.json()['data']:
            if item['attributes']['role'] == 'studio':
                link_two = item['relationships']['producer']['links']['related']
                res_two = requests.get(link_two)
                if res_two.status_code == 200 and res_two.json()['data'] != []:
                    studio = res_two.json()[
                        'data']['attributes'].get('name')
        if 'studio' not in locals():
            studio = 'Not Available'
        else:
            studio = 'Not Available'
        return studio
