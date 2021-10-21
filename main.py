import requests
import discord
from discord.ext import commands
from randomdog import RandomDog
from discordbot import DiscordBot
import random
from MagicBall import MagicBall
import json


def main():
    bot = DiscordBot("https://discord.com/api","Token goes Here")
    bot.botReady()
main()
