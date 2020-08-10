import discord
from discord import Client

client: Client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith(".투표"):
        vote = message.content[4:].split(".")
        await message.channel.send('투표 주제' + ' = ' + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send('```' + vote[i] + '```')
        await message.channel.send("(원하는 이모지를 추가하시오.)")


client.run("NzMwNjg1MzEzNDU3ODQ4MzYw.XwbFug.9PInyRyT3k3ErHEdUlngW3nBojc")
