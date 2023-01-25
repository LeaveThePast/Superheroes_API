import requests
import collections


def superheroes_api():
    url = 'https://akabab.github.io/superhero-api/api'
    heroes = {'Hulk': '332.json', 'Captain_America': '149.json', 'Thanos': '655.json', }
    powerstats = {}
    for hero in heroes:
        result = requests.get(url=url + '/powerstats/' + heroes[hero])
        result_json = result.json()
        powerstats[hero] = result_json['intelligence']
        sorted_heroes = dict(sorted(powerstats.items(), key=lambda item: item[1]))
    last = collections.deque(sorted_heroes, maxlen=1)
    print(f'Самый умный из выбранных супергероев: {last[0]}')


if __name__ == '__main__':
    superheroes_api()
