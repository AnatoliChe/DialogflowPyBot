#!/usr/bin/python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='TOKEN FOR TELEGRAM')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    print ('connected ', update.message.from_user, update.message.location)
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    print ('rcvd ', update.message.text_html, ' from: ', update.message.from_user)
    request = apiai.ApiAI('TOKEN API DialogFlow').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'IDBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
#    request.session_id = 'Weather' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update.message.text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    print ("answer = ", response)
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')
def developer(bot, update, chat_data):
    response = 'Mesage to user with USER_ID?'
    print ('rcvd from developer ' + response + ' from: ', update.message.from_user)
    bot.send_message(chat_id=USER_ID, text=response) #USER
    


print ("Bot started. Ctl+c to exit")
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(CommandHandler("developer", developer, pass_chat_data=True))
updater.start_polling(clean=True)
updater.idle()
