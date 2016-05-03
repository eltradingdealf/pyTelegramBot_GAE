#!C:/DEV/Python27
# -*- coding: utf-8 -*-
""" Programa de prueba de Bot. Envía un mensaje al Bot
    Es casi mi primer programa python, tendra cosas mejorables.
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

#Constantes
FILE_CONFIG_APP = "config.cfg"
TEST_MESSAGE = "/send envio de mensaje-4";

#globals
chatID = 0

#limpia los datos de la consola
def clearScreen():

    os.system('cls' if os.name=='nt' else 'clear')

#fin clearScreen


#Funcion que lee el archivo de configuracion de la app
#return obj @string with token value
def readTokenFromConfigFile():

    try:
        print '\n***'
        print 'ENV PATH=' + os.getcwd()
        print '***'
    except Exception as ex:
        print repr(ex)
        return None

    try:
        cfg = ConfigParser.ConfigParser()
        cfg.read([FILE_CONFIG_APP])

        print '\n***'
        print 'Config file readed'
        print '***'
    except Exception:
        print 'Error obteniendo archivo de config'

    return cfg
#fin readTokenFromConfigFile


#@return 0 sent, 1 not sent
def sendMessageBOT(_token, _chatID):

    print '\n***'
    print 'token=' + _token
    print 'chatID=' + _chatID
    print '***'

    try:
        telegram = telebot.TeleBot(_token)
        telegram.send_message(_chatID, TEST_MESSAGE)
    except telebot.apihelper.ApiException as ex:
        print repr(ex)
        return 1
    except Exception as ex:
        print "Unexpected Error:"
        print repr(ex)

    return 0
#fin sendMessageBOT


##--MAIN--###

clearScreen()
print 'program starting...'

#Leemos Token de Fichero de Config
cfg = readTokenFromConfigFile()
token = cfg.get("telegram","token")
chatID = cfg.get("telegram","chatid")

if (token is not None):
    #Enviamos el mensaje al Bot
    code = sendMessageBOT(token, chatID)

    if(1 == code):
        print '\n***'
        print 'Error Sending Message'
        print '\n***'
    else:
        print '\n***'
        print 'message sent'
        print '\n***'
else:
    print '\n***'
    print 'No token, message was not sent'
    print '\n***'

print '\nprogram terminating'
