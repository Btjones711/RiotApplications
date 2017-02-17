"""RiotAPI.py
created 1/31/2017
Library of Functions to work with Riot API
Author: Brendan Jones
"""
import requests

from api import API_KEY as key

API_key = key.getAPI_KEY()
Region = "na"
Host = "na.api.pvp.net"


def findChampionID(Key, Region):
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/champion?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj['data'][Key]['id']

def getChampionData(ChampionID, Region):
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/champion/" + ChampionID + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getSummonerID(summonerNames, Region):
    names = ""
    for name in summonerNames:
        names = names + "," + name

    url = "https://" + Host + "/api/lol/" + Region + "/v1.4/summoner/by-name/" + names + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    id_list = []
    for i in range(len(summonerNames)):
        id_list.append(json_obj[summonerNames[i].lower()]['id'])
    return id_list

def getSummonerNames(summonerIDs, Region):
    ID_list = str(summonerIDs[0])
    for ID in summonerIDs[1:]:
        ID_list += "," + str(ID)
    url = "https://" + Host + "/api/lol/" + Region + "/v1.4/summoner/" + ID_list + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    name_list = []
    for i in range(len(summonerIDs)):
        name_list.append(json_obj[str(summonerIDs[i])]["name"])
    return name_list


def getRecentGames(summonerID, Region):
    summonerID = str(summonerID)
    url = "https://" + Host + "/api/lol/" + Region + "/v1.3/game/by-summoner/" + summonerID + "/recent" + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

if __name__ == "__main__":
    test_find = findChampionID("Jax", Region)
    assert(test_find == 24)
    assert(getSummonerID(["BruttonGuster"],Region) == [68191523])
    my_id = getSummonerID(["BruttonGuster"],Region)
    x = getRecentGames(my_id[0], Region)['games']
    # ip_sum = 0
    # number = 0
    # for i in range(len(x)):
    #     print(x[i]['ipEarned'])
    #     ip_sum += x[i]['ipEarned']
    #     number += 1
    # print(ip_sum/number)
    print getSummonerNames([68191523],Region)[0]
