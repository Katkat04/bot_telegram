import os 
import dotenv
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import commands as bot

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')

def main():
    # Connect the bot 
    updater = Updater(TOKEN, use_context=True)
    des = updater.dispatcher

    # Comandos de ejecucion
    des.add_handler(CommandHandler("start", bot.start))
    des.add_handler(CommandHandler("ayuda", bot.ayuda))
    des.add_handler(CommandHandler("univariado", bot.univariado))
    #des.add_handler(CommandHandler("bivariado", bot.descifrar))
    #des.add_handler(CommandHandler("describe", bot.descifrar))

    # Respuestas a los callback
    des.add_handler(CallbackQueryHandler(bot.helpfuntion, pattern='Ayuda_univariado'))
    des.add_handler(CallbackQueryHandler(bot.helpfuntion, pattern='Ayuda_bivariado'))
    des.add_handler(CallbackQueryHandler(bot.helpfuntion, pattern='Ayuda_descripcion'))


    # Iniciar el bot
    updater.start_polling()

    # Mantiene el bot ejecutado hasta que ocurra una interrupción
    updater.idle()

if __name__ == '__main__':
    main()



