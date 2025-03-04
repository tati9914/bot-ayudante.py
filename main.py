import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'BIENVENIDO! TE HAS CONECTADO Y EL BOT ESTA FUNCIONANDO {bot.user}')

@bot.command('hola')
async def hola(ctx):
    await ctx.send('Hola soy el bot de discord, en q l@ asist@')

@bot.command('aleatorio')
async def aleatorio(ctx, minimo:int, maximo:int):
    num = random.randint(minimo, maximo)
    texto = f'el numero generado es: {num}'
    await ctx.send(texto)

@bot.command('gen_pass')
async def gen_pass(ctx, pass_length: int):
    elements = "+-/*!&$#?=@<>"
    password = ''.join(random.choice(elements) for _ in range(pass_length))
    await ctx.send(f'Contraseña generada: {password}')

@bot.command('frase')
async def frase(ctx):
    citas = [
        "La vida es 10% lo que te sucede y 90% cómo reaccionas a ello. – Charles R. Swindoll",
        "El único modo de hacer un gran trabajo es amar lo que haces. – Steve Jobs",
        "El futuro pertenece a aquellos que creen en la belleza de sus sueños. – Eleanor Roosevelt",
        "No se trata de si van a derribarte, se trata de si vas a levantarte cuando lo hagan» —Vince Lombardi"
    ]
    cita = random.choice(citas)
    await ctx.send(f"Cita inspiradora: {cita}")

@bot.command('broma')
async def broma(ctx):
    chistes = [
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Por qué el libro de matemáticas está estresado? Porque tenía demasiados problemas.",
        "¿Cuál es el café más peligroso del mundo? El ex-preso."
    ]
    chiste = random.choice(chistes)
    await ctx.send(f"Chiste: {chiste}")

@bot.command('meme_random')
async def mem(ctx):
    lista_imagenes = ['./images/meme1.jpg', './images/meme2.jpg', './images/meme3.jpg', './images/cat.png']
    imagen = random.choice(lista_imagenes)
    with open(imagen, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('ayudante')
async def ayudante(ctx):
    await ctx.send('BIENVENIDO!SOY UN BOT ASISTENTE, VENGO A INFORMATE SOBRE ALGUNO DE LOS SIGUIENTES TEMAS:\n'
                   '$COMPOSTAJE\n$RECICLAJE\n$CALENTAMIENTO GLOBAL\nESCRIBE EL QUE GUSTES')

@bot.command('COMPOSTAJE')
async def compostaje(ctx):
    await ctx.send('El compostaje es un proceso natural de descomposición de materia orgánica, como restos de comida, hojas y residuos de jardín, que se transforma en un abono rico en nutrientes. Al descomponerse, los microorganismos, como bacterias y hongos, desintegran los materiales orgánicos, generando compost, un fertilizante ecológico que mejora la calidad del suelo. Este proceso contribuye a reducir la cantidad de residuos en vertederos, disminuyendo la contaminación y promoviendo prácticas más sostenibles en el manejo de residuos. Si deseas saber cómo hacer compost, escribe $compostera')

@bot.command('RECICLAJE')
async def reciclaje(ctx):
    await ctx.send('El reciclaje es el proceso de recolectar, transformar y reutilizar materiales desechados, como papel, plástico, vidrio y metales, para convertirlos en nuevos productos. Este proceso ayuda a reducir la cantidad de residuos en vertederos, conserva recursos naturales, y disminuye la contaminación. Al reciclar, también se ahorran energía y se promueve un entorno más sostenible, contribuyendo a la protección del planeta para las futuras generaciones. Si deseas saber más, escribe $tipos_de_residuos')

@bot.command('CALENTAMIENTO_GLOBAL')
async def calentamiento_global(ctx):
    await ctx.send('El calentamiento global es el aumento sostenido de las temperaturas promedio de la Tierra debido a la acumulación de gases de efecto invernadero, como el dióxido de carbono, metano y óxidos de nitrógeno, en la atmósfera. Estos gases provienen principalmente de actividades humanas, como la quema de combustibles fósiles, la deforestación y la agricultura intensiva. El calentamiento global provoca cambios climáticos extremos, como olas de calor, sequías, inundaciones y el derretimiento de los glaciares, lo que pone en riesgo los ecosistemas y la vida humana en todo el mundo. Si deseas saber qué hacer para prevenirlo, escribe $prevenciones')

# Manejando imágenes para el tema de compostaje
@bot.command('compostera')
async def compostera(ctx):
    with open('imagen.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

# Manejando imágenes para el tema de calentamiento global
@bot.command('calentamiento_imagen')
async def calentamiento_imagen(ctx):
    with open('calentamientog.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

# Manejando imágenes de reciclaje
@bot.command('reciclaje_imagen')
async def reciclaje_imagen(ctx):
    with open('post-reciclaje.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture
