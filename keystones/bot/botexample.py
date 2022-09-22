import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTAxNjgxNzExNDYyNTA5Nzg3OQ.GqBl81.E_r63vHbwqZxvPY2KWz2u4pR318GPDfCOkFIp4')
