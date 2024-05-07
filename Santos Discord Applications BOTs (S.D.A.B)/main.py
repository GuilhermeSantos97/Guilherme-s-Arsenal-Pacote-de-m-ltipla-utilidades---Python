# Pip install discord.py.
# Aqui ele vai importar a biblioteca discord.
import discord
import time 
import nacl

from discord.ext import commands, tasks
from itertools import cycle
from colorama import init, Fore, Back, Style
from discord import FFmpegPCMAudio


# Inicializa colorama de uma maneira correta.
init()


# Aqui será definido um link direcionado p/ o meu GitHUB
redirect_url = "https://github.com/GuilhermeSantos97"


# Configurações do BOT intents
intents = discord.Intents.all()
intents.members = True

# Configuração do BOT (Comandos e eventos de atividade)
bot = commands.Bot(command_prefix = '>', intents=discord.Intents.all()) #comando prefixo é definido '>'
bot_status = cycle([">help for commands", "It s Brazil my Dudes"]) # Aqui ocorrerá a troca de status, posso tocar toda vez se caso eu não goste do anterior.




#1.     ------------------- SESSÃO DE EVENTOS -------------------------------</>

@tasks.loop(seconds=5)
async def troca_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))


# Eventos do BOT
@bot.event
async def on_ready():
    print(Fore.GREEN +"Sucesso:" + Fore.RED + "Client" + Fore.GREEN + " do BOT está Online ao Discord" + Fore.RESET) 
    print(Fore.MAGENTA + "---------------------< / >------------------------")
    print(Fore.LIGHTRED_EX + "Versão do discord.py está na:" + discord.__version__ )
    print(Fore.CYAN + f"Clique no link para visitar o meu Perfil do GitHub: {redirect_url}")
    troca_status.start() # Aqui ocorrerá a troca de status toda vez, em ciclos.

# Eventos do BOT (Membros)
@bot.event
async def on_member_join(member):
    await member.send("test")



#2.  ----------------- CONVERSAS BONITAS ---------------------------------</>

@bot.command(aliases=["ola", "olá", "Ola", "Oi", "oi"]) #Dentro do conchetos terá multiplas funções do nome ola!
async def Olá(ctx):
    await ctx.send(f"> Olá, novo mundo. Prazer meu nome é Paladino, como vai você {ctx.author.mention}!") # Aqui ele vai dizer e vai mencionar o autor.!


@bot.command(aliases=["Dia", "dia"])
async def BomDia(ctx):
    await ctx.send(f"> Bom dia {ctx.author.mention}Como vai?") # Aqui ele vai dizer e vai mencionar o autor.!


@bot.command(aliases=["Tarde", "tarde"])
async def BoaTarde(ctx):
    await ctx.send(f"> Boa Tarde{ctx.author.mention}Como vai?!") # Aqui ele vai dizer e vai mencionar o autor.!


@bot.command(aliases=["noite", "Noite"])
async def BoaNoite(ctx):
    await ctx.send(f"> Boa noite {ctx.author.mention}Como vai?!") # Aqui ele vai dizer e vai mencionar o autor.!



# </> -------------------- EXTRAS COMANDOS ------------------------- </>
@bot.command(aliases=["-dev", "--DEV"])
async def infoDev(ctx):
    await ctx.send(f"Prazer {ctx.author.mention} meu nome é Paladino, eu foi criado pelo Guilherme Santos!.") 
    await ctx.send(f"> veja as nossas redes sociais {ctx.author.mention}:")
    await ctx.send("> Instagram https://www.instagram.com/its_guill.of/")
    await ctx.send("> GitHUB (DEV): https://github.com/GuilhermeSantos97")


@bot.command(aliases=["-v", "--version"])
async def infoversion(ctx):
    await ctx.send(f"> Olá Guerreiro! {ctx.author.mention}, Paladino Delta está na versão = 1.11") 


@bot.command()
async def triggered(ctx):
	vc = await ctx.message.author.voice.channel.connect()
	
	time.sleep(1.5)
	await vc.disconnect()


#3. ------------- COMANDOS CHAT DE VOZ -------------------------------------

@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Shop.mp3')
        player = voice.play(source)
    else:
        await ctx.send("Testando")


@bot.command(pass_context = True)
async def saia(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Eu sai do canal de Voz")
    else:
        await ctx.send("Eu não estou no canal de Voz")


# </> --------------------- Registro ------------------------- </>

#Aqui ele exibirá o erro de uma forma mais dinâmica.
try:
    with open('discord_token.txt') as f: # O 'f' é definido como "file".
        token = f.read() # Variavel chamada de Token. O Read vai ler o arquivo dentro do '()'

except FileNotFoundError as error: # Aqui ele exibirá se caso ele não encotre o arquivo.
    print(error)
    print(Fore.RED + 'Deu ruim patrão, por favor de uma olhada no código e tente novamente!' + Fore.RESET) # Menssagem para o usuário.

bot.run(token)


#4. ----------------- EVENTOS DE REMOÇÃO ---------------------------------</>

# @bot.event
# async def on_message(message):
#     if message.content == "teste":
#         await message.delete()
#         await message.channel.send("Não envie xingamentos, caso contrário haverá ações ⚆ _ ⚆")