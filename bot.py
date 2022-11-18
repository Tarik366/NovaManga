import time
import discord
from discord import *
from discord.ext import commands, tasks
import os.path
from dotenv.main import load_dotenv
import datetime as dt
import requests
import feedparser
from bs4 import BeautifulSoup

a = 1034908325336334389 
intents = Intents.all()
Bot = commands.Bot("!", help_command=None, intents=intents)
load_dotenv()

@Bot.event
async def on_ready():
    NF = feedparser.parse("https://nova-manga.com/feed/")
    fentry = NF.entries[0]
    msg1.start()

@tasks.loop(minutes=1)
async def msg1():
    NF = feedparser.parse("https://nova-manga.com/feed/")
    entry = NF.entries[0]
    le = open("lastEntry.txt", "r", encoding="utf-8")
    ar = le.read()
    sentry = entry.title
    if sentry not in str(ar):
        class n:
            title = entry.title
            link = entry.link
            cat = entry.category
            catt = cat.replace(" ", "-")
            catt = catt.replace("'", "").lower()

        h = "https://nova-manga.com.com/manga/" + n.catt + "/"
        print(h)

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        sou = requests.get(h, headers=headers)
        soup = BeautifulSoup(sou.content, 'html.parser')
        im = ["a"]
        for s in soup.find_all("div", class_="thumb"):
            for item in s.find_all('img', class_="wp-post-image"):
                i = item['src']
                im = im + i.split("\n")
                print(im[1])
        n.img = im[1]
        emed = Embed(title=f"{entry.title} yayında keyifli okumalar!", description=f"okumak için {entry.link}", url=entry.link)
        emed = emed.set_image(url = n.img)
        channel = Bot.get_channel(a)
        print(str(ar))
        with open("lastEntry.txt", "w", encoding="utf-8") as wle:
            wle.write(n.title)
        await channel.send(embed=emed)
    print("a")


Bot.run(os.getenv('token')) 