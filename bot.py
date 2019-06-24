import discord
from discord.ext import commands
# import mysql.connector
# import random
# import time
# from discord.ext.commands import Bot
# from discord.utils import get
# import requests

token = "hidden"

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


@client.command()
async def help():
    embed = discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name='ServerTemplate Help')
    embed.add_field(name="test", value="owo", inline=False)
    await client.say(embed=embed)


@client.command(pass_context=True)
async def test(ctx, name):
    print('owo')

client.run(token)
