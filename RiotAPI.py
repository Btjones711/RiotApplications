"""RiotAPI.py
created 1/31/2017
Library of Functions to work with Riot API
Author: Brendan Jones
"""
import requests

from api import API_KEY as key

API_key = key.getAPI_KEY()
Region = "na"
platformID = "na1"
Host = "na.api.pvp.net"


def findChampionID(Key, Region='na'):
    """
    Function to retrieve Champion ID# based on champion key, usually name(i.e. jax gives 24)
    only exception I know of at the moment is 'Monkey King' for wukong
    input: Key, Region strings
    Output: ID integer
    """
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/champion?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj['data'][Key]['id']

def getChampionData(ChampionID, Region='na'):
    """
    Function to retrieve Champion data based on champion ID. Returns stats in form of JSON file. Print it to console
    to explore more.
    input: ChampionID integer, Region string
    Output: Data JSON
    """
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/champion/" + str(ChampionID) + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getSummonerID(summonerNames, Region='na'):
    """
    Function to retrieve Summoner IDs from a list of summoner names.
    Returns a list of summoner id's in the same order of names given
    input: summonerName list[strings], Region string
    Output: id_list list[integers]
    """
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

def getSummonerNames(summonerIDs, Region='na'):
    """
    Function to retrieve summoner names from a list of Summoner IDs.
    Returns a list of summoner names's in the same order of ID's given
    input: summonerIDs list[strings], Region string
    Output: name_list list[integers]
    """
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


def getRecentGames(summonerID, Region='na'):
    """
    Function to retrieve Recent games from a Summoner ID.
    Returns a JSON of recent games. Print to learn more.
    input: summonerID integer, Region string
    Output: json_obj JSON
    """
    summonerID = str(summonerID)
    url = "https://" + Host + "/api/lol/" + Region + "/v1.3/game/by-summoner/" + summonerID + "/recent" + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getRankedStats(summonerID, Region='na'):
    """
    Function to retrieve ranked stats from a Summoner ID.
    Returns a JSON of stats. Print to learn more.
    input: summonerID integer, Region string
    Output: json_obj JSON
    """
    summonerID = str(summonerID)
    url = "https://" + Host + "/api/lol/" + Region + "/v1.3/stats/by-summoner/" + summonerID + "/ranked" + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getMasteries(summonerIDs, Region='na'):
    """
    Function to retrieve materies from a Summoner ID.
    Returns a JSON of masteries. Print to learn more.
    to retreive pages call getMasteries(summonerIDs, Region)['pages'] then you can cycle through the pages
    input: summonerID integer, Region string
    Output: json_obj JSON
    """
    ID_list = str(summonerIDs[0])
    for ID in summonerIDs[1:]:
        ID_list += "," + str(ID)
    url = "https://" + Host + "/api/lol/" + Region + "/v1.4/summoner/" + ID_list + "/masteries?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    mast_list = []
    for i in range(len(summonerIDs)):
        mast_list.append(json_obj[str(summonerIDs[i])])
    return mast_list

def getRunes(summonerIDs, Region='na'):
    """
    Function to retrieve runes from a Summoner ID.
    Returns a JSON of runes. Print to learn more.
    to retreive pages call getRunes(summonerIDs, Region)['pages'] then you can cycle through the pages
    input: summonerID integer, Region string
    Output: json_obj JSON
    """
    ID_list = str(summonerIDs[0])
    for ID in summonerIDs[1:]:
        ID_list += "," + str(ID)
    url = "https://" + Host + "/api/lol/" + Region + "/v1.4/summoner/" + ID_list + "/runes?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    rune_list = []
    for i in range(len(summonerIDs)):
        rune_list.append(json_obj[str(summonerIDs[i])])
    return rune_list

def getRuneData(ID, Region='na'):
    """
    Function to retrieve rune data based on champion ID. Returns stats in form of JSON file. Print it to console
    to explore more.
    input: ID integer, Region string
    Output: Data JSON
    """
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/rune/" + str(
        ID) + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getMasteryData(ID, Region='na'):
    """
    Function to retrieve rune data based on rune ID. Returns stats in form of JSON file. Print it to console
    to explore more.
    To get name of mastery getMasteryData(ID,Region)['name']
    input: ID integer, Region string
    Output: Data JSON
    """
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/mastery/" + str(
        ID) + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getItemData(ID, Region='na'):
    """
    Function to retrieve item data based on item ID. Returns stats in form of JSON file. Print it to console
    to explore more.
    To get name of item getItemData(ID,Region)['name']
    input: ID integer, Region string
    Output: Data JSON
    """
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/item/" + str(
        ID) + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getItemList(Region='na'):
    """
    Function to retrieve item data based on item ID. Returns stats in form of JSON file. Print it to console
    to explore more.
    To get name of item getItemData(ID,Region)['name']
    input: ID integer, Region string
    Output: Data JSON
    """
    url = "https://" + Host + "/api/lol/static-data/" + Region + "/v1.2/item/?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

def getCurrentGameData(summonerID, platformID='na1'):
    """
    Function to retrieve current game data based on summoner ID. Returns stats in form of JSON file. Print it to console
    to explore more.
    input: summonerID integer, platformID string
    Output: Data JSON
    """
    url = "https://" + Host + "/observer-mode/rest/consumer/getSpectatorGameInfo/" + platformID + \
          "/" + str(summonerID) + "?api_key=" + API_key
    r = requests.get(url)
    json_obj = r.json()
    return json_obj

######Unit tesiting area######
if __name__ == "__main__":
    test_find = findChampionID("Jax", Region)
    assert(test_find == 24)
    assert(getSummonerID(["BruttonGuster"],Region) == [68191523])
    my_id = getSummonerID(["BruttonGuster"],Region)
    x = getRecentGames(my_id[0], Region)['games']

    assert(getSummonerNames([68191523],Region)[0] == "BruttonGuster")
    # print getRankedStats(68191523,Region)['champions'][0]
    # print getRankedStats(68191523,Region)['champions'][0]['id']
    # print getChampionData(getRankedStats(68191523,Region)['champions'][0]['id'], Region)
    # print getMasteries([68191523],Region)
    # print getRunes([68191523],Region)
    assert(getRuneData(5245, Region)['name'] == 'Greater Mark of Attack Damage')
    assert(getMasteryData(6121, Region)['name'] == 'Fresh Blood')
    # print(getItemList(Region))
    assert(getItemData(1400,Region)['name'] == 'Enchantment: Warrior')
    #print(getCurrentGameData(68191523))
    # TODO Find a way to test current game data. May just have to test while in game.
    # could test against twitch streamers on their daily schedule
