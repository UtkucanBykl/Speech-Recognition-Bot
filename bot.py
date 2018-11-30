from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tools import convert_ogg_to_wav, clear_directory
from const import  TOKEN
from Speech import Speech

updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher
speech = Speech()



def audio(bot, update):

    newFile = bot.getFile(update.message.voice.file_id)
    newFile.download("voicee.ogg")
    new = convert_ogg_to_wav("voicee.ogg", "voice.wav")
    speech.file = new
    text = speech.to_text()

    bot.sendMessage(chat_id = update.message.chat_id, text=text)

def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text="Bot çalışıyor.")


echo_handler = MessageHandler(Filters.voice, audio)
msg_handler = MessageHandler(Filters.text, start)



dispatcher.add_handler(echo_handler)
dispatcher.add_handler(msg_handler)

updater.start_polling()
