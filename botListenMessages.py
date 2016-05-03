#!C:/DEV/Python27
# -*- coding: utf-8 -*-
""" Este programa escucha mensajes al bot y
    responde con otro mensaje.
    ???Todavia no me funciona el 'message_handler'
    Nombre del bot de Telegram: eltradingdealf_bot
    Usuario de bot: eltradingdealf
    Token del bot: Se obtiene de config.cfg
    ChatID: se obtiene de config.cfg

    @author Alfredo Sanz
    @date Mayo 2016
"""

import telebot
import ConfigParser
import os
import smtplib

#Constantes
FILE_CONFIG_APP = "config.cfg"

#globals
chatID = 0
cfg = None
telegram = None

#limpia los datos de la consola
def clearScreen():

    os.system('cls' if os.name=='nt' else 'clear')

#fin clearScreen


def printM1(_mesg):

    print '\n***'
    print _mesg
    print '\n***'

#fin printM1


def printM2(_mesg1, _mesg2):

    print '\n***'
    print _mesg1 + "\n"
    print _mesg2
    print '\n***'

#fin printM2


#Funcion que lee el archivo de configuracion de la app
#return obj @string with token value
def readTokenFromConfigFile():

    try:
        printM1('ENV PATH=' + os.getcwd())
    except Exception as ex:
        print repr(ex)
        return None

    try:
        cfg = ConfigParser.ConfigParser()
        cfg.read([FILE_CONFIG_APP])

        printM1('Config file readed')
    except Exception as ex:
        print 'Error obteniendo archivo de config.'
        print repr(ex)

    return cfg
#fin readTokenFromConfigFile


#Connect to Telegram Bot and returns the telegram object
#@return Telegam Obj
def connectBot(_token):

    mytelegram = None
    try:
        mytelegram = telebot.TeleBot(_token)
        info_api = mytelegram.get_me() # Comprobar el API. Devuelve un objeto
    except telebot.apihelper.ApiException as ex:
        print ("Error conectando con el bot...")
        print repr(ex)

    return mytelegram
#fin connectBot


def listener(mensaje_telegram):

    printM1('listening messages')

    for mensaje in mensaje_telegram:
        chatID = mensaje.chat.id  #gets the chatid of the telegram user using the bot

        printM2('chatID='+str(chatID), 'mensaje=' + mensaje.text)

        if mensaje.content_type == 'text':
            try:
                printM1('Sending message to Bot')

                telegram.send_message(chatID, mensaje.text)
            except telebot.apihelper.ApiException as ex:
                print ("Error sending message to Bot.")
                print repr(ex)
        #if
    #for

#fin listener


###**--MAIN EXEC--**###

clearScreen()
printM1('program starting...')

#Leemos Token de Fichero de Config
cfg = readTokenFromConfigFile()
token = cfg.get("telegram","token")
chatID = cfg.get("telegram","chatid")

if (token is not None):
    printM1('Connecting to Bot')
    telegram = connectBot(token)

    if(telegram is not None):
        printM1('Registering listener')
        telegram.set_update_listener(listener)

        printM1('Polling')
        telegram.polling()
else:
    printM1('No token, message was not sent')

printM1('program terminating')


#???No funciona todavia
@telegram.message_handler(commands=['chat', 'corre'])
def chat(mensaje_telegram):

    printM1('chat method')
    chatID = mensaje_telegram.chat.id # <--- ChatID para todos los ejercicios
    printM1("chatID=" + str(chatID))

    printM1('Sending chat message to Bot')
    telegram.send_message(chatID, "oido cocina")
