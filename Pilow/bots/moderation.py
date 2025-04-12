import discord
from discord.ext import commands

token = "MTM2MDI1ODcyNTg4MDc5NTM5OA.Gyh8JG.BBAEUjwU3ifKOs5v4i6apvyXNfCw1Ed2javV4c"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'{member.name} a été exclu(e).')

bot.run(token=token) 