from steam import SteamID
from steam import WebAPI
from keys import steamKey
import re


STEAM_API_KEY = WebAPI(steamKey)

def idMapping(identifier):
    
    if identifier == None:
        return None
    
    elif re.match(r"https://steamcommunity\.com/id/[^/]+/",
         identifier) != None:
        return SteamID.from_url(identifier)

    elif re.match(r"https://steamcommunity\.com/profiles/[^/]+/",
         identifier) != None:
        return SteamID(identifier[36:-1])
    
    elif re.match(r"\d+", identifier) != None:
        return SteamID(identifier)

    elif re.match(r"\w+", identifier) != None:
        return SteamID.from_url("https://steamcommunity.com/id/" + identifier)

    else:
        return None


def mostPlayedGames(identifier, free):
    steamid = idMapping(identifier)

    if steamid == None:
        return "Invalid identifier"

    res_dict = STEAM_API_KEY.IPlayerService.GetOwnedGames(steamid=steamid,
     include_appinfo=1, include_played_free_games=free, include_free_sub=free, appids_filter=0)
    
    res_raw = []
    res = ""
    
    for i in res_dict["response"]["games"]:
        res_raw.append([i["name"], i["playtime_forever"] // 60])

    res_raw = sorted(res_raw, key=lambda x:x[1])
    res_raw.reverse()  
    
    for i in range(10):
        res += "%i) %s: %i hours\n" % (i + 1, res_raw[i][0], res_raw[i][1])

    return res


def getPlayerBans(identifier):
    steamid = idMapping(identifier)

    if steamid == None:
        return "Invalid identifier"

    res_dict = STEAM_API_KEY.ISteamUser.GetPlayerBans(steamids=steamid)
    res = "Bans info:\n"

    for i in res_dict["players"][0].keys():
        res += "%s: %s\n" % (i, str(res_dict["players"][0].get(i)))

    return res
