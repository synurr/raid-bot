import discord
from discord.ext import commands
import asyncio
import random
import datetime
import youtube_dl
import time 
import traceback
import dice
import logging
import pyfiglet
import os
from discord import Member
from discord import Guild

client = commands.Bot(command_prefix = '/')

players = {}

@client.event
async def on_ready():
    print('----------------------')
    print("""\
                                    
          o    |    |         |    
,---.,---..,---|    |---.,---.|--- 
|    ,---|||   |    |   ||   ||    
`    `---^``---'    `---'`---'`---'
""")
    print(f'Bot={client.user}')
    print('Ready to raid when you are ')
    print('----------------------')
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="porn"))


@client.command(pass_context=True)
async def raid(ctx):
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')


@client.command(pass_context=True)
async def ping(ctx):
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await ctx.send(f"ping= {ping}")

@client.command()
async def logout(ctx):
    await client.logout()

@client.command(pass_context=True)
async def clear(ctx, amount=500): 
        await ctx.channel.purge(limit=amount)
        await ctx.send('Deleted 500 messages or more ;)') 
        print('Deleted 500 messages or more ;)') 

@client.command(pass_context=True)
async def github(ctx):
    await ctx.send('https://github.com/synurr/discord-raid')
    print('Sent github link')

while 1:

    print(" ")
    try:
        print("please enter your token")
        client.run(input("> "))

    except Exception:
        print("the token was incorrect")


#make sure to install all the refrences using "pip install %refrence%
#for example, pip install logging

#print(f'{client.user}')

#installing pyfiglet is optional, basically that lets me convert normal text to ascii, there will be a file called raid(compatibility-version).py that doesnt print any ascii :) 