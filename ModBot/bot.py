import os
import discord

import discord.ext
import discord.ext.commands


with open("token", "r") as f:
    Token = f.read()

with open("suId", "r") as f:
    suId = f.read()

# Define the intents
intents = discord.Intents.all()
intents.members = True

bot = discord.ext.commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to server')

def is_allowed_user(ctx):
    return str(ctx.author.id) == suId

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def h(ctx):
    embed = discord.Embed(
        title="Hot Or Not Redux",
        description="Burn players if they carry hot fluids, the Temperature threshold can be configured currently 1300º (lava). It should work with any Fluid Containers that are properly coded.",
        color=discord.Color.blue()
    
    )
    embed.set_thumbnail(url='https://media.forgecdn.net/avatars/thumbnails/152/782/256/256/636613936490276739.png')
    embed.add_field(name="Curse Forge Download", value="[curseforge link](https://www.curseforge.com/minecraft/mc-mods/hot-or-not)", inline=False)
    embed.add_field(name="Github Repo", value="[github link](https://github.com/Porting-Dead-Mods/HotOrNotRedux)", inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()

def eCF(embed, str):
    embed.add_field(name="Curse Forge Download",value=f"[curseforge link]({str})", inline=False)
def eGH(embed, str):
    embed.add_field(name="Github Repo",value=f"[github link]({str})", inline=False)
def eThmub(embed,url):
    embed.set_thumbnail(url=url)



@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def b(ctx):
    e = discord.Embed(
        title="Bonsai Tree Crops",
        description=
        '''Bonsai Trees is a farming mod that adds a crop for each type of (vanilla) tree.
            This mod allows you to grow crop-based trees that produce bonsai clippings, which can be crafted into sticks and each wood variant.
        ''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/993/514/256/256/638508426835362184.png')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/bonsai-tree-crops-updated")
    eGH(e,"https://github.com/Porting-Dead-Mods/Bonsai")
    await ctx.send(embed=e)
    await ctx.message.delete()

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def dd(ctx):
    e = discord.Embed(
        title="DurabilityDisplay",
        description=
        '''This is a simple mod that will replace the regular durability or energy bar on items with a percentage value. This mod is a port of the original version, made for the GTNH Modpack''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/987/708/256/256/638498974950523682_animated.gif')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/durability-display")
    eGH(e,"https://github.com/Porting-Dead-Mods/DuraDisplay")
    await ctx.send(embed=e)
    await ctx.message.delete()

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def ib(ctx):
    e = discord.Embed(
        title="Inverted Beds",
        description=
        '''Inverted Bed is a simple mod that allows you to take naps in the day to skip it.''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/989/367/256/256/638501875637048418.png')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/inverted-bed")
    eGH(e,"https://github.com/Porting-Dead-Mods/InvertedBed")
    await ctx.send(embed=e)
    await ctx.message.delete()

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def mp(ctx):
    e = discord.Embed(
        title="More Plates Updated",
        description=
        '''This mod adds Gears, Plates and Rods''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/869/545/256/256/638284869036610964.png')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/more-plates-updated")
    eGH(e,"https://github.com/Porting-Dead-Mods/More-Plates")
    await ctx.send(embed=e)
    await ctx.message.delete()

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def ml(ctx):
    e = discord.Embed(
        title="Mana Liquidizer",
        description=
        '''This mod is a basic mod that allows you to turn mana into mana fluid (and vice versa!) through a block called the Mana Liquidizer''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/313/445/256/256/637408903476462924.png')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/mana-liquidizer")
    eGH(e,"https://github.com/Porting-Dead-Mods/Mana-Liquidizer-1.20.1")
    await ctx.send(embed=e)
    await ctx.message.delete()

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def mf(ctx):
    e = discord.Embed(
        title="MooFluids Modern",
        description=
        '''This mod adds cows for all types of fluids (even modded ones!). This allows farming these fluids easily.''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/1003/358/256/256/638524004079756924.png')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/moo-fluids-modern")
    eGH(e,"https://github.com/Porting-Dead-Mods/Fluid-Cows")
    await ctx.send(embed=e)
    await ctx.message.delete()

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def s(ctx):
    e = discord.Embed(
        title="Snad: Redstone Edition",
        description=
        '''The "Snad" block introduced by this mod will, as opposed to its cousin "Sand," accelerate up the growth  of sugarcane and cacti using redstone.''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/876/594/256/256/638300546125191741.png')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/snad-redstone-edition")
    eGH(e,"https://github.com/Leclowndu93150/Snad-Redstone-Edition")
    await ctx.send(embed=e)
    await ctx.message.delete()

@bot.command()
@discord.ext.commands.check(is_allowed_user)
async def inf(ctx):
    e = discord.Embed(
        title="Infinite Night Vision [FORGE/FABRIC]",
        description=
        '''The "Infinite Night Vision" mod grants players the ability to have unlimited night vision in Minecraft. With this mod, you can effortlessly see in the dark without the need for torches or other light sources, enhancing your exploration and gameplay experience during nighttime.''',
        color=discord.Color.blue()
    )
    eThmub(e,'https://media.forgecdn.net/avatars/thumbnails/852/991/256/256/638256239271576862.png')
    eCF(e,"https://www.curseforge.com/minecraft/mc-mods/infinite-night-vision")
    eGH(e,"https://github.com/Leclowndu93150/Infinite-Night-Vision")
    await ctx.send(embed=e)
    await ctx.message.delete()

bot.run(Token)