import requests
import discord
from discord.ext import commands
from randomdog import RandomDog
import random
from MagicBall import MagicBall
import json
import time
import os
from discord.ext.commands import Bot


class DiscordBot:
    def __init__(self,api_url,token):
        self.api_url = api_url
        self.token = token



    def botReady(self):
        client = commands.Bot(command_prefix = ".")
        @client.event
        async def on_ready():
            print("Bot Ready and has logged in as {0.user}".format(client))

        @client.command()
        async def ping(ctx):
            await ctx.send("**PONG**")
        @client.command()
        async def randomdog(ctx):
            random = RandomDog("https://dog.ceo/api/breeds/image/random")
            random.get()
            random.response()
            await ctx.send(random.answer())


        @client.command()
        async def yesorno(ctx, *, questions):
            ballAnswer = MagicBall("https://yesno.wtf/api")
            ballAnswer.get()
            ballAnswer.response()
            await ctx.send(f'Answer: {ballAnswer.answer()}')

        #a much less complicated way to incorperate a simple API into discord through json
        @client.command()
        async def quote(ctx):
            response = requests.get("https://zenquotes.io/api/random")
            json_data = json.loads(response.text)
            quote = json_data[0]['q']+ " -" + json_data[0]['a']
            await ctx.channel.send(quote)

        client.run(self.token)
