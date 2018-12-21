import requests
import json
f= open("Answer.txt","w+")
#a= open("Prediction.txt","w+")
parameter = ["teams"]
team1 = "Arsenal FC"
team2 = "Chelsea FC"
team1Rating = -1
team2Rating = -1
header = {"X-Auth-Token" : "1064e2f6968e4852bd573b410130ccae"}
url = "https://api.football-data.org/v2/competitions/PL/standings"
params = dict(
    name = team1
)

response = requests.get(url= url, params=params, headers= header)
data = response.json()

table = data['standings'][0]['table']

for elt in table:
    if elt['team']['name'] == team1:
        team1Rating = elt['position']
    elif elt['team']['name'] == team2:
        team2Rating = elt['position']

    if team1Rating != -1 and team2Rating != -1:
        break

# Assumes non-equal ranking
if team1Rating < team2Rating:
    f.write("Team 1 is better!")
else:
    f.write("Team 2 is better!")
