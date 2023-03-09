import requests
api_url = "https://www.dnd5eapi.co/api/spells"
response = requests.get(api_url).json()


spells = [(x['name'], x['url']) for x in response['results']]

selector = ['' for _ in range(response['count'])]
i=0

with open("spell_names.txt", 'w') as g:
    for x in spells:
        g.write(x[0] + "\n")
g.close()

with open("spells.txt", 'w') as f:
    for x in spells:
        responsex = requests.get('https://www.dnd5eapi.co' + x[1]).json()
        y = " ".join(responsex['desc']).replace('hit points', 'health (toughness)') + " " + " ".join(responsex['higher_level']) if responsex.__contains__('higher_level') else ""
        i += 1
        print('loading ' + x[0])
        f.write(y+"\n")
f.close()