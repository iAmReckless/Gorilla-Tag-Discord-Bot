import os
os.system("pip install py-cord==2.0.0b1")
import discord
import asyncio
import requests
import aiohttp
import json
import random
import time, datetime, requests
from discord.ext import commands, tasks

#bot = discord.Bot()
#intents = discord.Intents().all()
#bot = commands.Bot(command_prefix=',', intents=intents)

bot = commands.Bot(command_prefix='!')


@bot.event
async def bot_activity():
  await bot.wait_until_ready()
  while True:
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Loving Vicky ❤️"))
    await asyncio.sleep(10)

#@bot.event
#async def on_ready():
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} 
    #print("Online!")
    #servers = str(len(bot.guilds))
    #FortniteGame_Build = data["FortniteLive"]["version"]
    #await bot.change_presence(activity=discord.Game(name=f'{servers} servers'))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="AAA" 

 
    
footertext = "Made with ❤️ By Reckless#7785"
color = 0x5865F2

#@bot.event
#async def on_readyy():
    #print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    #await bot.change_presence(activity=discord.CustomActivity(name='Custom status' ,emoji='🔋'))

#@bot.slash_command(name="ping", description="Sends Bots Ping.")
#async def test(ctx):
    #await ctx.respond(f'bots ping is {round(bot.latency * 1000)}ms')


"""@bot.slash_command(name="dmall", description="dm all members")
async def mall(ctx):
    #await ctx.message.delete()
    for member in list(bot.get_all_members()):
        await asyncio.sleep(0)
        try:
            await member.send("🎁 Free Renegade Raider Accounts Vouch 1+ 🎁\n| https://discord.gg/7YyEnDmWwd")
        except:
            pass
        print("Action completed: Message all")"""

"""@bot.command()
async def invite(ctx):
embed = discord.Embed(
            color= discord.Colour.dark_teal() # or any color you want
        )
        embed.add_field(name='If you wish to add me in your server,' ,value='[Click here to add]()', inline=False)
        await ctx.send(embed=embed)"""
    
"""@bot.slash_command(name="help", description="Shows Help")
    embed=discord.Embed(title="Help", description='Top 10 Commands', color=0x000000)
    embed.add_field(name='Ban', value='Bans a Member')
    embed.add_field(name='Unban', value='Unbans a Member')
    embed.add_field(name='Kick', value='Kicks a Member')
    embed.add_field(name='Purge', value='Purge Messages')
    embed.add_field(name='Lock', value='Lock a Channel')
    embed.add_field(name='Unlock', value='Unlock a Channel')
    
    await ctx.send(embed=embed)"""
    
    
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


@bot.slash_command(name="ban", description="Ban Someone")
@commands.has_permissions(ban_members = True)
async def bn(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f"Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.respond(embed=ban)
        await user.respond(embed=ban)
        
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f"Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.send(embed=ban)
        await user.send(embed=ban)

        
@bot.slash_command(name="unban", description="Unban Someone")
@commands.has_permissions(ban_members = True)
async def unbn(ctx, id):
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        unban = discord.Embed(title=f"Unbanned {user.name}!", description=f"By: {ctx.author.mention}")
        #unban = discord.Embed(title=f"Unbanned {user.name}!")
        await ctx.respond(embed=unban)
        
@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, id):
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        unban = discord.Embed(title=f"Unbanned {user.name}!")
        await ctx.send(embed=unban)
        


@bot.slash_command(name="kick", description="Kick Someone")
@commands.has_permissions(kick_members = True)
async def kck(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f"Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.respond(embed=kick)
        await user.respond(embed=kick)

        
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f"Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.send(embed=kick)
        await user.send(embed=kick)



@bot.slash_command(name="purge", description="Purge Messages")
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.respond('Messages Purged by {}'.format(ctx.author.mention))
        #await ctx.message.delete()
        
@bot.command()      
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Messages Purged by {}'.format(ctx.author.mention))
        #await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
        
@bot.slash_command(name="lock", description="Lockdown a Channel")
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.respond( ctx.channel.mention + " ***is now in lockdown.***")
    
@bot.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in lockdown.***")


@bot.slash_command(name="unlock", description="Unlock a Channel")
@commands.has_permissions(manage_channels=True)
async def unlck(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.respond(ctx.channel.mention + " ***has been unlocked.***")
    
@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")

bot.loop.create_task(bot_activity())
        
bot.run("MTA3OTkzNTMwMTM2OTIwODk2Mg.G5dvP9.mC9L4k910aSmjy-Rl80MnnEe5qg9i5NC4KRgHA")