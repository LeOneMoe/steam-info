import re
import random
import asyncio
import steamMethods
from discord.ext.commands import Bot
from keys import discordKey

from datetime import datetime


start_time = datetime.now()

BOT_PREFIX = ("!", "?", "1")
TOKEN = discordKey


client = Bot(command_prefix=BOT_PREFIX)


# idk

def identityFormat(identity):
    
    if identity == None:
        return None
    
    elif re.match(r"https://steamcommunity\.com/id/[^/]+", identity) != None:
        return identity

    elif re.match(r"https://steamcommunity\.com/profiles/\d+", identity) != None:
        return identity

    elif re.match(r"\d+", identity) != None:
        return "https://steamcommunity.com/profiles/" + identity

    elif re.match(r"\w+", identity) != None:
        return "https://steamcommunity.com/id/" + identity

    else:
        return None


# Commands

@client.command(name="mostplayedgames",
                description="!command profileUrl/id add_free_games-optional\n\
                        Example: !games 76561198115601378 1",
                brief="Shows user top 10 most played games",
                aliases=["MostPlayedGames", "PlayedGames", "games"],
                pass_context=True)
async def MostPlayedGames(context, identity=None, free=0):
    print("%s: !MostPlayedGames %s %i" % (context.message.author, identity, free))

    identity = identityFormat(identity)

    if identity == None:
        await client.say("Invalind or on profileUrl/id")
        return 
    
    res = steamMethods.MostPlayedGames(identity, free)

    await client.say(context.message.author.mention + "\n" + res)   


@client.command(name="getplayerbans",
                description="!command profileUrl/id \n\
                        Example: !bans 76561198115601378",
                brief="Shows user bans info",
                aliases=["GetPlayerBans", "PlayedBans", "bans"],
                pass_context=True)
async def GetPlayerBans(context, identity=None):
    print("%s: !GetPlayerBans %s" % (context.message.author, identity))

    identity = identityFormat(identity)

    if identity == None:
        await client.say("Invalind or on profileUrl/id")
        return 

    res = steamMethods.GetPlayerBans(identity) 
    
    await client.say(context.message.author.mention + "\n" + res)


# Debugging

@client.event
async def on_ready():
    print("----------------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("----------------\n")


async def listServers():
    await client.wait_until_ready()
    await asyncio.sleep(1)

    while not client.is_closed:
        print("~~~~~~~~~~~~~~~~")
        print("Current servers: ")

        for server in client.servers:
            print(server.name)
        
        print("~~~~~~~~~~~~~~~~\n")
        
        await asyncio.sleep(600)


async def upTime():
    await client.wait_until_ready()
    await asyncio.sleep(1)

    while not client.is_closed:
        
        print("Current up time: {0}".format(datetime.now() - start_time), end="\r")

        await asyncio.sleep(1)


client.loop.create_task(listServers())
client.loop.create_task(upTime())
client.run(TOKEN)
