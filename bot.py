import os
from keep_alive import keep_alive
import time
import discord
from discord import *
from discord.ext import commands, tasks
from discord.utils import get
import os.path
from dotenv.main import load_dotenv
import datetime as dt
import requests
import feedparser
from bs4 import BeautifulSoup
from time import sleep
from os import system

load_dotenv()

a = 1034908325336334389
intents = discord.Intents.all()
Bot = commands.Bot("!", help_command=None, intents=intents)
load_dotenv()

@Bot.event
async def on_ready():
    NF = feedparser.parse("https://nova-manga.com/feed/")
    fentry = NF.entries[0]
    msg1.start()
    keep_alive()
   
class RolMenu(ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Japonca sohbet", style=ButtonStyle.grey)
    async def Japonca(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Japonca Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

@tasks.loop(seconds=3)
async def msg1():
    
    
    NF = feedparser.parse("https://nova-manga.com/feed/")
    entry = NF.entries[0]
    
    
    le = open("lastEntry.txt", "r", encoding="utf-8")
    ar = le.read()
    
    class n:
        title = entry.title
        link = entry.link
        cat = entry.category
        catt = cat.replace(" ", "-")
        catt = catt.replace("'", "").lower()
        
        
    h = "https://nova-manga.com/"
    sentry = entry.title
    
    
    if sentry not in str(ar):

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        sou = requests.get(h, headers=headers)
        soup = BeautifulSoup(sou.content, 'html.parser')
        
        def ws():
            for s in soup.find_all("div", class_="utao"):
                for item in s.find_all('img', class_="wp-post-image"):
                    i = item['src']
                    im = i.split("\n")
                    hgf = im[0]
                    print(hgf)
                    return hgf

        nimg = ws()
        emed = discord.Embed(title=f"{entry.title} yayında keyifli okumalar!", description=f"okumak için {entry.link}", url=entry.link)
        emed = emed.set_image(url = nimg)

        channel = Bot.get_channel(a)

        await channel.send(embed=emed)

        with open("lastEntry.txt", "w", encoding="utf-8") as wle:
            wle.write(sentry)

try:
    Bot.run(os.getenv('token'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW")
    system("python restarter.py")
    system('kill 1')
