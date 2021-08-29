print('Starting...')
with open('bot_token.txt') as f:
    botToken = f.readlines()

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'b!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for B\'s'))
    print('Ready!')

@client.event 
async def on_message(message):
    def split(content):
        return [char for char in content]

    msg = str(message.content)
    parsedMsg = split(msg)

    bCheck = False
    for x in range(0, len(parsedMsg)):
        if parsedMsg[x] == 'b' or parsedMsg[x] == 'B':
            parsedMsg[x] = '<:b:874974547877724230>'
            bCheck = True

    if bCheck == False:
        return
    if message.author == client.user:
        return
    if message.author.bot: return
    await message.channel.purge(limit = 1)

    finalMsg = ''.join(parsedMsg)

    content = []
    for w in await message.guild.webhooks():
        content.append([f"{w.name}", f"{w.id}"])

    webhookDetected = False

    for x in range(0, len(content)):
        if content[x][0] == 'BotDetectUser':
            webhookDetected = True
            webhookTemp = content[x][1]
    
    if webhookDetected == False:
        webhook = await message.channel.create_webhook(name='BotDetectUser')
    else:
        webhook = await client.fetch_webhook(webhookTemp)

    await webhook.send(content=finalMsg, username=message.author.name, avatar_url=message.author.avatar_url)

client.run(botToken[0])