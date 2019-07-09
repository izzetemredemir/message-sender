import steembase
from steem import Steem

client = Steem(keys=[''])

def send_steem(body,title):
	author = 'author name without @'
	body = body
	taglist = ['tr','busy']
	client.commit.post(title=title, body=body, author=author, tags=taglist)
	print("Post created successfully")

send_steem("Hello World", "Test content")

import discord
from discord.ext import commands
import asyncio

#https://discordapp.com/oauth2/authorize?client_id={bot-id}&scope=bot&permissions={permissions}

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

dc("Hello World")