import requests
import discord
from discord.ext import commands
from randomdog import RandomDog
import random
from MagicBall import MagicBall
import json


class DiscordBot:
    def __init__(self,api_url,token):
        self.api_url = api_url
        self.token = token
        

    def botReady(self):
        client = commands.Bot(command_prefix = ".")
        @client.event
        async def on_ready():
            print("Bot Ready")

        @client.command()
        async def randomdog(ctx):
            random = RandomDog("https://dog.ceo/api/breeds/image/random")
            random.get()
            random.response()
            await ctx.send(random.answer())

        @client.command()
        async def ping(ctx):
            await ctx.send("I dont really want to say it, but **PONG**...")

        @client.command()
        async def yesorno(ctx, *, questions):
            ballAnswer = MagicBall("https://yesno.wtf/api")
            ballAnswer.get()
            ballAnswer.response()
            await ctx.send(f'Answer: {ballAnswer.answer()}')

        client.run(self.token)
