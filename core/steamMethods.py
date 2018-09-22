import requests
from keys import steamKey

STEAM_API_KEY = steamKey

url = "http://api.steampowered.com/"


def getInfo(steamid, method_):

    

    payload = {"key": STEAM_API_KEY, "steamid": steamid, "format": "json", "include_appinfo": "1", "include_played_free_games": "1"}
    
    res_json = requests.get(url + method_, params=payload)

    return res_json


def MostPlayedGames(steamid):

    method_ = "IPlayerService/GetOwnedGames/v0001/"
    
    res_dict = getInfo(steamid, method_).json()

    res_raw = []

    res = ""

    for i in res_dict["response"]["games"]:
        res_raw.append([i["name"], i["playtime_forever"] // 60])

    res_raw = sorted(res_raw, key=lambda x:x[1])
    res_raw.reverse()

    for i in range(10):
        res += "%i) %s: %i hours\n" % (i + 1, res_raw[i][0], res_raw[i][1])

    return res
