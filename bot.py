import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents = discord.Intents.all()) # .ban/ !ban/ $ban
bot.remove_command("help") #В help показываются все команды. Нам это не нужно!

@bot.event
async def on_ready():
    print("Im ready!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(933077870224490576)
    role = member.guild.get_role(role_id = 933090967286870096)
    await channel.send(f"{member.name} Добро пожаловать на сервер!")
    await member.add_roles(role)

bot.run("OTMyMjI0NzU5MzY0NzMwOTMw.YeP39g.h73eg0ziB7XKrXnnbV-CMamZWTc")