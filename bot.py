import discord
from discord.ext import commands
# import mysql.connector
# import random
# import time
# from discord.ext.commands import Bot
# from discord.utils import get
# import requests

token = ""

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
    embed.add_field(name="!tmp gaming", value="A template for g@m3rs", inline=False)
    embed.add_field(name="!tmp social", value="A template for friends", inline=False)
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def tmp(ctx, name=""):

    if name == "":
        await ctx.send("The template command needs an argument following `!tmp` for example `!tmp gaming`")

    elif name == "gaming":
        guild = ctx.guild
        await ctx.send(":video_game:")

        role_admin = await guild.create_role(name="Admin", permissions=discord.Permissions(permissions=8), hoist=True)
        role_modo = await guild.create_role(name="Moderator", permissions=discord.Permissions(permissions=1341648327), hoist=True)
        role_member = await guild.create_role(name="Member", permissions=discord.Permissions(permissions=104320064), hoist=True)

        overwrites_admin = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            role_member: discord.PermissionOverwrite(read_messages=False),
            role_modo: discord.PermissionOverwrite(read_messages=False)
        }

        overwrites_mods = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            role_member: discord.PermissionOverwrite(read_messages=False),
            role_modo: discord.PermissionOverwrite(read_messages=True)
        }

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            role_member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            role_modo: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        overwrites_welcome = {
            guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            role_member: discord.PermissionOverwrite(read_messages=False),
            role_modo: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        overwrites_announcement = {
            guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False),
            role_member: discord.PermissionOverwrite(read_messages=True, send_messages=False),
            role_modo: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        cat_admins = await guild.create_category('admin')

        admin = await guild.create_text_channel('Admins', overwrites=overwrites_admin)
        await admin.edit(category=cat_admins)

        bot_admin = await guild.create_text_channel('Bot-Commands-Admins', overwrites=overwrites_admin)
        await bot_admin.edit(category=cat_admins)

        mods = await guild.create_text_channel('Mods', overwrites=overwrites_mods)
        await mods.edit(category=cat_admins)

        voice_admin = await guild.create_voice_channel('Admins', overwrites=overwrites_admin)
        await voice_admin.edit(category=cat_admins)

        voice_mods = await guild.create_voice_channel('Mods', overwrites=overwrites_mods)
        await voice_mods.edit(category=cat_admins)

        cat_welcome = await guild.create_category('welcome')

        rules = await guild.create_text_channel('Rules', overwrites=overwrites_announcement)
        await rules.edit(category=cat_welcome)

        announcements = await guild.create_text_channel('Announcements', overwrites=overwrites_announcement)
        await announcements.edit(category=cat_welcome)

        welcome = await guild.create_text_channel('Welcome', overwrites=overwrites_welcome)
        await welcome.edit(category=cat_welcome)

        general = await guild.create_text_channel('General', overwrites=overwrites)
        await general.edit(category=cat_welcome)

        cat_games = await guild.create_category('games')

        game1 = await guild.create_text_channel('Game-1', overwrites=overwrites)
        await game1.edit(category=cat_games)

        game2 = await guild.create_text_channel('Game-2', overwrites=overwrites)
        await game2.edit(category=cat_games)

        game3 = await guild.create_text_channel('Game-3', overwrites=overwrites)
        await game3.edit(category=cat_games)

        game4 = await guild.create_text_channel('Game-4', overwrites=overwrites)
        await game4.edit(category=cat_games)

        cat_other = await guild.create_category('other')

        off = await guild.create_text_channel('Off-Topic', overwrites=overwrites)
        await off.edit(category=cat_other)

        bot = await guild.create_text_channel('Bot-Commands', overwrites=overwrites)
        await bot.edit(category=cat_other)

        cat_voice = await guild.create_category('voice')

        voice1 = await guild.create_voice_channel('Voice-1', overwrites=overwrites)
        await voice1.edit(category=cat_voice)

        voice2 = await guild.create_voice_channel('Voice-2', overwrites=overwrites)
        await voice2.edit(category=cat_voice)

        voice3 = await guild.create_voice_channel('Voice-3', overwrites=overwrites)
        await voice3.edit(category=cat_voice)

        voice4 = await guild.create_voice_channel('Voice-4', overwrites=overwrites)
        await voice4.edit(category=cat_voice)

        voice5 = await guild.create_voice_channel('Voice-5', overwrites=overwrites)
        await voice5.edit(category=cat_voice)

        voice6 = await guild.create_voice_channel('Voice-6', overwrites=overwrites)
        await voice6.edit(category=cat_voice)

    else:
        await ctx.send("The template you're looking for doesn't exist, you can find available templates here : "
                       "https://discordapp.com/templates (actually it doesn't exist yet)")

client.run(token)
