import discord
from discord.ext import commands
from os import getenv
import re


client = commands.Bot(command_prefix='!')
TOKEN = getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_member_join(member):
    verified = discord.utils.get(member.server.roles, name="verified")
    if not verified in member.roles:
        #Verification process
        await member.send('Are you real?')
        msg = await client.wait_for('message')
        if msg.content in ['yes', 'y']:
            await member.add_roles(verified)
    else:
        await member.send('You are already verified!')

async def on_member_remove(member):
    verified = discord.utils.get(member.server.roles, name="verified")
    await member.remove_roles(verified)


client.run(TOKEN)