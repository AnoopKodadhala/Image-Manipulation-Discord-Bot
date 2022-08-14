import discord
from discord.ext import commands
import asyncio
from io import BytesIO
from PIL import Image

client = discord.Client()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Image Manipulator Discord Bot is now running'.format(client))




@client.command()
async def darker(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    darker = Image.open('black-transparent.png')

    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    '''pfp = pfp.resize((177.177))'''
    darker.paste(pfp, (120, 212))
    darker.save("profile.png")

    await ctx.send(file = discord.File('profile.png'))

async def pfp(ctx, user: discord.Member = None ):
    if user == None:
        user = ctx.author

    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((177.177))
    pfp.save("profile.png")

    await ctx.send(file=discord.File(pfp))

client.run('MTAwODI1NDM4ODQzMjgwMTgzMg.GNwEjM.WNnQaMK_KwnUYE48Wc5hXxj_6a9vuIAZYYZP10')
