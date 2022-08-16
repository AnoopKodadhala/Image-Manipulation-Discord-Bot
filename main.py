import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageEnhance, ImageOps, ImageFont, ImageDraw
import textwrap

client = discord.Client()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Image Manipulator Discord Bot is now running'.format(client))

@client.command()
async def pfp(ctx, user: discord.Member = None ):
    if user == None:
        user = ctx.author

    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((177, 177))
    pfp.save("export.png")

    await ctx.send(file=discord.File('export.png'))

@client.command()
async def darker(ctx, user: discord.Member = None):
    files = []
    attachments = ctx.message.attachments
    if attachments == files:
        if user == None:
            user = ctx.author
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((177,177))
        pfp.save("export.png")
        enhancer = ImageEnhance.Brightness(pfp)
        im_output = enhancer.enhance(0.3)
        im_output.save('export.png')

        await ctx.send(file = discord.File('export.png'))
    else:
        for attachment in ctx.message.attachments:
            await attachment.save('export.png')
        userImage = Image.open('export.png')
        enhancer = ImageEnhance.Brightness(userImage)
        im_output = enhancer.enhance(0.3)
        im_output.save('export.png')
        await ctx.send(file=discord.File('export.png'))

@client.command()
async def brighter(ctx, user: discord.Member = None):
    files = []
    attachments = ctx.message.attachments
    if attachments == files:
        if user == None:
            user = ctx.author
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((177,177))
        pfp.save("export.png")
        enhancer = ImageEnhance.Brightness(pfp)
        im_output = enhancer.enhance(1.7)
        im_output.save('export.png')

        await ctx.send(file = discord.File('export.png'))
    else:
        for attachment in ctx.message.attachments:
            await attachment.save('export.png')
        userImage = Image.open('export.png')
        enhancer = ImageEnhance.Brightness(userImage)
        im_output = enhancer.enhance(1.7)
        im_output.save('export.png')
        await ctx.send(file=discord.File('export.png'))

@client.command()
async def grayscale(ctx, user: discord.Member = None):
    files  = []
    attachments = ctx.message.attachments
    if attachments == files:
        if user == None:
            user = ctx.author
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((177,177))
        pfp = ImageOps.grayscale(pfp)
        pfp.save('export.png')
        await ctx.send(file=discord.File('export.png'))
    else:
        for attachment in ctx.message.attachments:
            await attachment.save('export.png')
        userImage = Image.open('export.png')
        userImage = ImageOps.grayscale(userImage)
        userImage.save('export.png')

        await ctx.send(file=discord.File('export.png'))

@client.command()
async def toptext(ctx, *,user_msg: str):
    for attachment in ctx.message.attachments:
        await attachment.save('export.png')
    userImage = Image.open('export.png')
    draw1 = ImageDraw.Draw(userImage)
    x,y = userImage.size
    x2 = x//2
    y2 = y//20
    fontSize = 75
    while True:
        font1 = ImageFont.truetype("AlfaSlabOne-Regular.ttf",fontSize)
        print(draw1.textbbox((0,0) , text = user_msg, font=font1,))
        if draw1.textlength(user_msg, font=font1,)  >= y:
            fontSize -= 7
        else:
            break
    font1 = ImageFont.truetype("AlfaSlabOne-Regular.ttf", fontSize)
    draw1.text((x2,y2),user_msg,(255,255,255),anchor='mt', font=font1, )
    userImage.save('export.png')

    await ctx.send(file=discord.File('export.png'))

@client.command()
async def bottomtext(ctx, *,user_msg: str):
    for attachment in ctx.message.attachments:
        await attachment.save('export.png')
    userImage = Image.open('export.png')
    draw1 = ImageDraw.Draw(userImage)
    x,y = userImage.size
    x2 = x//2
    y2 = y//20
    fontSize = 75
    while True:
        font1 = ImageFont.truetype("AlfaSlabOne-Regular.ttf",fontSize)
        print(draw1.textbbox((0,0) , text = user_msg, font=font1,))
        if draw1.textlength(user_msg, font=font1,)  >= y:
            fontSize -= 7
        else:
            break
    font1 = ImageFont.truetype("AlfaSlabOne-Regular.ttf", fontSize)
    draw1.text((x2,y),user_msg,(255,255,255),anchor='ms', font=font1, )
    userImage.save('export.png')

    await ctx.send(file=discord.File('export.png'))


@client.command()
async def send_file(ctx, *,user_msg: str):
    attachments = ctx.message.attachments
    files = []
    for attachment in ctx.message.attachments:
        await attachment.save('export.png')
    for attachment in attachments:
        files.append(await attachment.to_file())

    if files:
        await ctx.send(user_msg, files=files)
    else:
        await ctx.send(user_msg)

client.run('MTAwODI1NDM4ODQzMjgwMTgzMg.GNwEjM.WNnQaMK_KwnUYE48Wc5hXxj_6a9vuIAZYYZP10')
