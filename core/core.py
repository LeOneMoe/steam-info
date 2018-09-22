import random
from discord.ext.commands import Bot
import steamMethods
from keys import discordKey


BOT_PREFIX = ("!", "?", "1")
TOKEN = discordKey


client = Bot(command_prefix=BOT_PREFIX)

@client.command(name="mostplayedgames",
                description="Shows user top 10 most played games (need steam_id)",
                aliases=["MostPlayedGames", "PlayedGames", "games"])
async def MostPlayedGames(steamid):

    res = steamMethods.MostPlayedGames(steamid)

    await client.say(res)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
