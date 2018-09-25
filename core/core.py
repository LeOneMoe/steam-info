import random
import asyncio
import steamMethods
from discord.ext.commands import Bot
from keys import discordKey


BOT_PREFIX = ("!", "?", "1")
TOKEN = discordKey


client = Bot(command_prefix=BOT_PREFIX)


# Commands

@client.command(name="mostplayedgames",
                description="!command steamid add_free_games-optional\n\
                        Example: !games 76561198115601378 1",
                brief="Shows user top 10 most played games",
                aliases=["MostPlayedGames", "PlayedGames", "games"],
                pass_context=True)
async def MostPlayedGames(context, steamid=None, free=0):
    print("%s: !MostPlayedGames %s %i" % (context.message.author, steamid, free))

    if steamid == None:
        await client.say("You did`n specify steamid")
        return 
    
    res = steamMethods.MostPlayedGames(steamid, free)

    await client.say(context.message.author.mention + "\n" + res)   


@client.command(name="getplayerbans",
                description="!command steamid \n\
                        Example: !bans 76561198115601378",
                brief="Shows user bans info",
                aliases=["GetPlayerBans", "PlayedBans", "bans"],
                pass_context=True)
async def GetPlayerBans(context, steamid=None):
    print("%s: !GetPlayerBans %s" % (context.message.author, steamid))

    if steamid == None:
        await client.say("You did`n specify steamid")
        return 

    res = steamMethods.GetPlayerBans(steamid) 
    
    await client.say(context.message.author.mention + "\n" + res)


# Вebugging

@client.event
async def on_ready():
    print("----------------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("----------------")


async def list_servers():
    await client.wait_until_ready()
    await asyncio.sleep(1)

    while not client.is_closed:
        print("~~~~~~~~~~~~~~~~")
        print("Current servers: ")

        for server in client.servers:
            print(server.name, end="\n")
        
        print("~~~~~~~~~~~~~~~~")
        await asyncio.sleep(60)


client.loop.create_task(list_servers())
client.run(TOKEN)
