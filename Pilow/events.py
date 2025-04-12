import discord

token = "MTM2MDI1ODcyNTg4MDc5NTM5OA.Gyh8JG.BBAEUjwU3ifKOs5v4i6apvyXNfCw1Ed2javV4c"  # Remplacez par un token valide

# Activez TOUS les intents + message_content
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")  # Confirme la connexion

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:  # Ignore les messages du bot
        return
    
    if message.content.lower().startswith("bonjour"):
        await message.channel.send("Bonjour, c'est Pilow !")


@client.event
async def on_message_delete(message: discord.Message):
    await message.channel.send(f"{message.author.name} +  a supprimé son message :  + {message.content}")

@client.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    await after.channel.send(f"{before.content} a supprimé son message : {after.content}")

client.run(token)
