"""DailyIP.py
Program written to do the backend calculations for a daily IP calculator
Brendan Jones
3/8/2017 -started ground work and function layout
"""

import RiotAPI as RA
import time
current_time = time.time()


def getTimePlayed(json_index):
    """Function that returns the time played of a given game
    input: json_index from getRecentGames ex: getRecentGames[0] for most recent game
    output: integer of length of game in seconds
    """
    return json_index['stats']['timePlayed']


def getEndDate(json_index):
    """Function that returns the end time of a given game
    input: json_index from getRecentGames ex: getRecentGames[0] for most recent game
    output: integer of end game in milliseconds from epoch
    """
    return json_index['createDate']


def getDateOfGame(time_played, end_date):
    """Function that returns the date and time of a given game by converting from milliseconds from epoch
    input: json_index from getRecentGames ex: getRecentGames[0] for most recent game
    output: integer of end game in milliseconds from epoch
    """
    return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(end_date/1000 - time_played))[5:16]

def getIP(json_index):
    return json_index['ipEarned']


def check_date(dateOne, dateTwo):
    return dateOne == dateTwo

def sum_daily_ip(recentGames, date):
    sum1 = 0
    for i in range(len(recentGames)):
        current = recentGames[i]
        time_played = getTimePlayed(current)
        end_date = getEndDate(current)
        if check_date(getDateOfGame(time_played, end_date),date):
            sum1 += getIP(current)
    return sum1

######Unit tesiting area######
if __name__ == "__main__":
    my_id = RA.getSummonerID(["BruttonGuster"])
    x = RA.getRecentGames(my_id[0])['games']
    print(x)
    print(getDateOfGame(getTimePlayed(x[9]), getEndDate(x[9])))
    print(sum_daily_ip(x,"08 Mar 2017"))
