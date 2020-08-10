import discord
import os
from discord import Client

client: Client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith("GYCG 투표"):
        vote = message.content[8:].split(".")
        await message.channel.send('투표 주제' + ' = ' + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send('```' + vote[i] + '```')
        await message.channel.send("(원하는 이모지를 추가하시오.)")

    if message.content.startswith("gycg 투표"):
        vote = message.content[8:].split(".")
        await message.channel.send('투표 주제' + ' = ' + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send('```' + vote[i] + '```')
        await message.channel.send("(원하는 이모지를 추가하시오.)")

    if message.content.startswith("/..공지.."):
        channelid = "742189410501525514"
        msg = message.content[8:]
        await client.get_channel(int(channelid)).send(msg)

access_token = os.environ("BOT_TOKEN")
client.run(access_token)
