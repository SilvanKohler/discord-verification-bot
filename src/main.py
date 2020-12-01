import discord
from discord.ext import commands
from os import getenv
import re
from mail import send

client = commands.Bot(command_prefix='!')
TOKEN = getenv('DISCORD_TOKEN')
VERIFICATION_CHANNEL_ID = 783389199499526206 # Production
VERIFICATION_CHANNEL_ID = 783362942527078481 # Developement


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

def is_channel(ctx):
    return ctx.channel.id == VERIFICATION_CHANNEL_ID

@client.command()
@commands.check(is_channel)
async def verify(ctx):
    verified = discord.utils.get(ctx.guild.roles, name="verified")
    if not verified in ctx.author.roles:
        await ctx.send('Verification has been sent in DM.')
        #Verification process
        #
        await ctx.author.send('What\'s your GIBB E-Mail?')
        #
        #
        msg = await client.wait_for('message')
        if True or re.match('[a-z][a-z][a-z][0-9][0-9][0-9][0-9][0-9][0-9]@stud.gibb.ch', msg.content) or re.match('[a-z][a-z][a-z][0-9][0-9][0-9][0-9][0-9][0-9]@iet-gibb.ch', msg.content):
            await ctx.author.send('A E-Mail is on its way.')
            #await ctx.author.send('You shall pass!')
            send(msg.content)
            #await ctx.author.add_roles(verified)
        else:
            await ctx.author.send('You shall not pass!')

    else:
        await ctx.send('You are already verified!')



client.run(TOKEN)