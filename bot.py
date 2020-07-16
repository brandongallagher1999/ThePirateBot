import discord
from discord.ext import commands
from modules.pirate_api import Pirate_API
from discord import Embed
import datetime
server = commands.Bot(command_prefix="!!")

pirateAPI = Pirate_API()

token: str = ""
with open("config.txt", "r") as f:
    token = str(f.readlines()[0])

@server.command()
# WIP
async def help(ctx):
    embed = Embed()

    embed.set_author(name="ThePirateBot")
    embed.add_field(name="Display Torrent Info", value ="")

@server.command()
async def torrent(ctx, *args) -> str:
    
    if (len(args) < 1):
        await ctx.send("Please provide the name of the torrent (movie/game/etc)")
    else:
        try:
            query: str = ""
            for string in args:
                query += " " + string

            torrent: dict = pirateAPI.get_torrent(query)[0]

            embed = discord.Embed()
            embed.set_image(url=torrent["image_url"])
            embed.set_author(name=args[0])
            embed.set_footer(text=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            embed.add_field(name="Name", value=torrent["name"], inline=False)
            embed.add_field(name="Magnet", value=torrent["magnet"], inline=False)

            await ctx.send(embed=embed)
        except:
            await ctx.send("Torrent not found, please try another query.")


server.run(token)