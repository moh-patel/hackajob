import requests

response = requests.get("https://raw.githubusercontent.com/openfootball/football.json/198f60ce50ac427dadc16a35ef4ad65edcea3125/2014-15/en.1.json")

js_obj = response.json()

print(len(js_obj))

print(js_obj.keys())

print(len(js_obj['rounds']))

print(js_obj['rounds'][37])
print(js_obj['rounds'][37].keys())


# rounds iterate through iter
# mathes 

team = 'arsenal'
goals = 0
for round in js_obj['rounds']:
    # print('round',round)
    # print(round['matches'])
    for match in round['matches']:
        if match['team1']['key'] == team:
            print(match)
            goals+=match['score1']
            break
        elif match['team2']['key'] == team:
            goals+=match['score2']
            print(match)
            break

print(goals)
        # print(match['team1']['key'])
        # print(match['team2']['key'])
        # print(match['score1'])
        # print(match['score2'])