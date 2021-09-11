import discord
from discord.ext import commands
from modules.pirate_api import Pirate_API
from discord import Embed
import requests
import urllib
import datetime
server = commands.Bot(command_prefix=".")

pirateAPI = Pirate_API()

token: str = ""
with open("config.txt", "r") as f:
    token = str(f.readlines()[0])


def shorten(magnet: str) -> str:

    temp: str = urllib.parse.quote(magnet)
    return requests.get(f"http://mgnet.me/api/create?&format=json&opt=&m={temp}&_=1595006240839",
    headers = {
              "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
              "accept-language": "en-US,en;q=0.9",
              "x-requested-with": "XMLHttpRequest",
              
    }).json()["shorturl"]


@server.command()
async def tpb(ctx, *args) -> str:
    
    if (len(args) < 1):
        await ctx.send("Please provide the name of the torrent (movie/game/etc)")
    else:
        try:
            query: str = ""
            for string in args:
                query += " " + string

            torrent: dict = pirateAPI.get_torrent(query)[0]
            magnet = shorten(torrent["magnet"])

            embed = discord.Embed()
            embed.set_image(url=torrent["image_url"])
            embed.set_author(name=ctx.message.author)
            embed.set_footer(text=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            embed.add_field(name = "Name", value = torrent["name"], inline = False)
            embed.add_field(name = "Magnet", value = magnet, inline = False)

            await ctx.send(embed=embed)
        except:
            await ctx.send("Torrent not found, please try another query.")


server.run(token)
