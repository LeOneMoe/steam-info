import requests
from keys import steamKey


STEAM_API_KEY = steamKey
url = "http://api.steampowered.com/"


def getInfo(steamid, method_, payload):    
    res_json = requests.get(url + method_, params=payload)

    return res_json


def MostPlayedGames(steamid, free):
    method_ = "IPlayerService/GetOwnedGames/v0001/"
    payload = {"key": STEAM_API_KEY, "steamid": steamid, "include_appinfo": "1", "include_played_free_games": free, "format": "json"}
    
    res_dict = getInfo(steamid, method_, payload).json()
    res_raw = []
    res = ""

    for i in res_dict["response"]["games"]:
        res_raw.append([i["name"], i["playtime_forever"] // 60])

    res_raw = sorted(res_raw, key=lambda x:x[1])
    res_raw.reverse()

    for i in range(10):
        res += "%i) %s: %i hours\n" % (i + 1, res_raw[i][0], res_raw[i][1])

    return res


def GetPlayerBans(steamid):
    method_ = "ISteamUser/GetPlayerBans/v1/"
    payload = {"key": STEAM_API_KEY, "steamids": steamid}

    res_dict = getInfo(steamid, method_, payload).json()
    res_raw = []
    res = "Bans info:\n"

    for i in res_dict["players"][0].keys():
        res += "%s: %s\n" % (i, str(res_dict["players"][0].get(i)))

    return res
