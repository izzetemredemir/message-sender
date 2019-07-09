import telebot
import tweepy
import steembase
from steem import Steem
from mastodon import Mastodon
import discord
from discord.ext import commands
import asyncio

#https://discordapp.com/oauth2/authorize?client_id={bot-id}&scope=bot&permissions={permissions}


# Twitter
# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
# Create API object
api = tweepy.API(auth)

#Steem
client = Steem(keys=[''])

#Telegram
token = ""

def tele(message):
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id="", text=message)

def send_steem(body,title):
    author = 'author name without @'
    body = body
    taglist = ['tr','busy']
    client.commit.post(title=title, body=body, author=author, tags=taglist)
    print("Post created successfully")


def send_tweet(message):
    api.update_status(message)

def tooth(message):
    mastodon = Mastodon(
        access_token='',
        api_base_url='https://mastodon.social'
    )
    mastodon.toot(message)

# This code send message to all servers and just a text channel which is general.
def dc(message):
    token = ""
    client = discord.Client()
    channel = discord.TextChannel

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        await sendm(message)

    async def sendm(message):
        for guild in client.guilds:
            for channel in guild.text_channels:
                # It just send message to text or general text channels.
                if (channel.name == 'text' or channel.name == 'general'):
                    await channel.send(message)
        await  client.close()
    client.run(token)

tele("Hello World")
dc("Hello World")
send_tweet("Hello World")
send_steem("Hello World", "Test content")
tooth("Hello World")
