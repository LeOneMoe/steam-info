import requests
from steam import SteamID
from steam import WebAPI
from keys import steamKey


STEAM_API_KEY = WebAPI(steamKey)
url = "http://api.steampowered.com/"

def idMapping(identity):
    pass


def getInfo(steamid, method_, payload):    
    res_json = requests.get(url + method_, params=payload)

    return res_json


def MostPlayedGames(profileUrl, free):
    steamid = SteamID.from_url(profileUrl)

    res_dict = STEAM_API_KEY.IPlayerService.GetOwnedGames(steamid=steamid, include_appinfo=1, include_played_free_games=free, appids_filter=0)
    res_raw = []
    res = ""
    
    for i in res_dict["response"]["games"]:
        res_raw.append([i["name"], i["playtime_forever"] // 60])

    res_raw = sorted(res_raw, key=lambda x:x[1])
    res_raw.reverse()  
    
    for i in range(10):
        res += "%i) %s: %i hours\n" % (i + 1, res_raw[i][0], res_raw[i][1])

    return res


def GetPlayerBans(profileUrl):
    steamid = SteamID.from_url(profileUrl)

    res_dict = STEAM_API_KEY.ISteamUser.GetPlayerBans(steamids=steamid)
    res_raw = []
    res = "Bans info:\n"

    for i in res_dict["players"][0].keys():
        res += "%s: %s\n" % (i, str(res_dict["players"][0].get(i)))

    return res
