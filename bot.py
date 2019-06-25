import discord
from discord.ext import commands
# import mysql.connector
# import random
# import time
# from discord.ext.commands import Bot
# from discord.utils import get
# import requests

token = "No_Token_For_You"

Client = discord.Client()
client = commands.Bot(command_prefix='!')
client.remove_command('help')

# bdd = mysql.connector.connect(user='', password='', host='', database='')
# cursor = bdd.cursor()
# request = ""
# cursor.execute(request)
# bdd.commit()
# cursor.close()


@client.event
async def on_ready():
    ready = "Ready !" + "\nBot name : " + str(client.user.name) + "\nBot ID : " + str(client.user.id)
    print(ready)


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name='ServerTemplate Help')
    embed.add_field(name="test", value="owo", inline=False)
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def tmp(ctx, name=""):
    if name == "":
        await ctx.send("The template command needs an argument following `!tmp` for example `!tmp gaming`")
    elif name == "gaming":
        guild = ctx.guild
        await ctx.send(":video_game:")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        cat_welcome = await guild.create_category('welcome')
        rules = await guild.create_text_channel('Rules', overwrites=overwrites)
        announcements = await guild.create_text_channel('Announcements', overwrites=overwrites)
        welcome = await guild.create_text_channel('Welcome', overwrites=overwrites)

        await rules.edit(category=cat_welcome)
        await announcements.edit(category=cat_welcome)
        await welcome.edit(category=cat_welcome)

    else:
        await ctx.send("The template you're looking for doesn't exist, you can find available templates here : "
                       "https://discordapp.com/templates (actually it doesn't exist yet)")

client.run(token)
