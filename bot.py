import time
import discord
from discord import *
from discord.ext import commands, tasks
import os.path
from dotenv.main import load_dotenv
import datetime as dt
import feedparser
from RSS import *

a = 1034908325336334389 
intents = Intents.all()
Bot = commands.Bot("!", help_command=None, intents=intents)
load_dotenv()

@Bot.event
async def on_ready():
    NF = feedparser.parse("https://nova-manga.com/feed/")
    fentry = NF.entries[0]
    msg1.start()

@tasks.loop(minutes=5)
async def msg1():
    NF = feedparser.parse("https://nova-manga.com/feed/")
    entry = NF.entries[0]
    le = open("lastEntry.txt", "r")
    ar = le.read()
    sentry = str(entry)
    if sentry not in ar:
        emed = Embed(title=f"{entry.title} yayında keyifli okumalar!", description=f"okumak için {entry.link}", url=entry.link)
        emed = emed.set_image(url = n.img)
        channel = Bot.get_channel(a)
        print(emed)
        wle = open("lastEntry.txt", "w")
        wle.write(sentry)
        wle.close


@Bot.command()
async def o(ctx):
    emed = Embed(title=f"{n.title} yayında keyifli okumalar!", description=f"okumak için {n.link}", url=n.link)
    emed = emed.set_image(url = n.img)
    await ctx.send(embed=emed)

Bot.run(os.getenv('token')) 