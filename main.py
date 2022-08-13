"""
PUBG Map Maker for NA Pro Scrims - 8/12/2022
"""
import discord
from PIL import Image, ImageFont, ImageDraw
from keys import token
import asyncio
import io

erangelCopy = Image.open('Erangel.png') # Creating the copy of the map
title_text = "Test" # Creating text to put onto the copied map
# Creating the font size:
fontsize = 75
font = ImageFont.truetype("arial.ttf", fontsize)
image_editable = ImageDraw.Draw(erangelCopy)
image_editable.text((2200,2150), title_text, fill=255, font=font) # Write the text onto the map
erangelCopy.save("result.png") # Save the new map

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith(".map"):
            with open('result.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)

client = MyClient()
client.run(token)
