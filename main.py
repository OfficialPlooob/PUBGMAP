"""
PUBG Map Maker for NA Pro Scrims - 8/12/2022
"""
import discord
import asyncio
import io
from PIL import Image, ImageFont, ImageDraw
from keys import token
from COORDS import *

erangelCopy = Image.open('Erangel.png') # Creating the copy of the map
title_text = "Test"
fontsize = 75
font = ImageFont.truetype("arial.ttf", fontsize)
image_editable = ImageDraw.Draw(erangelCopy)
color = (247,191,7)
image_editable.Imagecolor("#E3FD34")
image_editable.text((670,980), title_text, fill=255, font=font)
erangelCopy.save("result.png")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith(".map"):
            with open('result.png', 'rb') as f:
                picture = discord.File(f)
                print(picture)
                await message.channel.send(file=picture)


client = MyClient()
client.run(token)
