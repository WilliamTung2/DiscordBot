import requests
import discord
from discord.ext import commands
from randomdog import RandomDog
from discordbot import DiscordBot
import random
from MagicBall import MagicBall
import json


def main():
    bot = DiscordBot("https://discord.com/api","Token goes Here") #for privacy reasons, token was not allowed to be uploaded
    bot.botReady()
main()
