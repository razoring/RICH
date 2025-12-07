import discord
from discord.ext import commands
from discord import app_commands
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name="status", description="Prints debug information.")
async def status(interaction: discord.Interaction):
    await interaction.response.send_message(f"W.I.M.P.(Weighted Index Market Predictor)\nLast Updated: {datetime.date}\nhttps://github.com/razoring/WIMP")

bot.run(TOKEN)