import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')


@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam!")


@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")



bot.run("BOTUNUZUN TOKEN BURADA OLMALIDIR!")
