import requests
import collections

resp = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
resp_json = resp.json()


def best_superhero(names_superheroes, powerstat):
    superheroes_powerstat = {}
    for name_superhero in names_superheroes:
        for superhero in resp_json:
            if name_superhero == superhero['name']:
                superheroes_powerstat[superhero['powerstats'][powerstat]] = name_superhero
    sort = sorted(superheroes_powerstat.items(), reverse=True)
    return f"Самый лучший в категории '{powerstat}' является {sort[0][1]}."


print(best_superhero(['Hulk', 'Captain America', 'Thanos'], 'intelligence'))








