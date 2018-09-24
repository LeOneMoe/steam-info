import random
from discord.ext.commands import Bot
import steamMethods
from keys import discordKey


BOT_PREFIX = ("!", "?", "1")
TOKEN = discordKey


client = Bot(command_prefix=BOT_PREFIX)

@client.command(name="mostplayedgames",
                description="!command steamid add_free_games-optional\n\
                        Example: !games 76561198115601378 1",
                brief="Shows user top 10 most played games",
                aliases=["MostPlayedGames", "PlayedGames", "games"])
async def MostPlayedGames(steamid=None, free=0):
    if steamid == None:
        await client.say("You did`n specify steamid")
        return 
    
    res = steamMethods.MostPlayedGames(steamid, free)

    await client.say(res)   


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
