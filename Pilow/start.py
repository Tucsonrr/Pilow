import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()
token = "MTM2MDI1ODcyNTg4MDc5NTM5OA.Gyh8JG.BBAEUjwU3ifKOs5v4i6apvyXNfCw1Ed2javV4c"

class MonBot(commands.Bot):
  async def setup_hook(self):
    for extension in ['games', 'moderation']:
      await self.load_extension(f'cogs.{extension}')

intents = discord.Intents.all()
bot = MonBot(command_prefix='!', intents=intents)

keep_alive()
bot.run(token=token)