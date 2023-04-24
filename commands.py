import logging
import traceback
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio.log import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def start(update, context):
    nombre_usuario = update.message.chat.first_name
    logger.info(f"El usuario {nombre_usuario} ha iniciado el BOT")
    update.message.reply_text(f'Hola {nombre_usuario}, gracias por usar nuestro Bot, para conocer las funciones de nuestro bot puedes solicitar el menu de ayuda con este comando /ayuda')
    logger.info("El bot ha sido iniciado ")

def ayuda(update, context):
    name= update.message.chat.first_name 
    logger.info(f"<the user{name} has solicited help>")
    buttons = [ 
        [InlineKeyboardButton("Univariado", callback_data= 'Ayuda_univariado')],
        [InlineKeyboardButton("Bivariado", callback_data='Ayuda_bivariado')],
        [InlineKeyboardButton("Descripción", callback_data='Ayuda_descripcion')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(
        "has solicitado el menú de ayuda:",  
    reply_markup = reply_markup
    )
    logger.info("<Se ha desplegado el menu de ayuda>")
    

def helpfuntion(update, context):
    query = update.callback_query
    query.answer()
    callback = query.data
    if callback == 'Ayuda_univariado':
        univariadoinfo(query)
    elif callback == 'Ayuda_bivariado':
        bivariadoinfo(query)
    else:
       callback == 'Ayuda_descripción'
       describirinfo(query)

def univariadoinfo(query):
    name = query.message.chat.first_name
    logger.info(f'<The user {name} called help for univariadoinfo>')
    message = f"""
    \¡Bienvenidx {name}\!, a continuación te explicaré como utilizar el comando univariado\:

    El comando univariado lo que hace es imprimir una grafica , el usuario debe escribir\:
    /univariado    
    """
    query.message.reply_text(message, parse_mode='MarkdownV2')

def bivariadoinfo(query):
    name=query.message.chat.first_name
    logger.info(f"<the user{name} has call bivariadoinfo>")
    message = f"""
    \¡Bienvenidx {name}\!, a continuación te explicaré como utilizar el comando bivariado\:

    El comando bivariado, lo que hace es imprimir una grafica luego de haber ingresado los 2 datos necesarios, para usarlo, lo que hacemos es escribir el comando\:
    /bivariado    
    """
    query.message.reply_text(message, parse_mode='MarkdownV2')

def describirinfo(query):
    name= query.message.chat.first_name
    logger.info(f"<the user{name} has call describirinfo>")
    message = f"""
    \¡Bienvenidx {name}\!, a continuación te explicaré como utilizar el comando univariado\:

    Para graficar, el usuario debe escribir\:
    /describe    
    """
    query.message.reply_text(message, parse_mode='MarkdownV2')

def univariado(update, context):
    nombre_usuario = update.message.chat.first_name
    logger.info(f"El usuario {nombre_usuario} ha llamado la función cifrar ")
    text = update.message.text
    text = text.replace("/univariado", "").strip()
    datos = text.split(";")

def bivariado(update, context):
    nombre_usuario = update.message.chat.first_name
    logger.info(f"El usuario {nombre_usuario} ha llamado la función cifrar ")
    text = update.message.text
    text = text.replace("/bivariado", "").strip()
    datos = text.split(";")
