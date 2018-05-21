import telebot
from telebot import types
import time
import requests
import json
import os

TOKEN=os.environ['keyT']

administrador = ###### <--- mi id de Telegram

usuarios = [line.rstrip('\n') for line in open('usuarios.txt')]
 
bot = telebot.TeleBot(TOKEN)

#############################################
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if not str(cid) in usuarios:
        usuarios.append(str(cid))
        aux = open( 'usuarios.txt', 'a')
        aux.write( str(m.from_user.first_name) + " " + str(cid) + "\n")
        aux.close()
        bot.send_message( cid, "Bienvenido al bot de Lenguaje de Marcas")
#############################################
#Listener
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print(mensaje)
 
bot.set_update_listener(listener)
#############################################

#Funciones de prueba
@bot.message_handler(commands=['holamundo'])
def command_foto(m):
    cid = m.chat.id
    bot.send_photo( cid, open( 'wallpaper-784710.jpg', 'rb'))
 
@bot.message_handler(commands=['holamundotext'])
def command_holamundotexto(m): 
    cid = m.chat.id
    bot.send_message( cid, 'Prueba de texto')
    
#############################################
#Funcion para difundir mensajes
@bot.message_handler(commands=['all'])
def command_all(m):
    cid = m.chat.id
    if cid != administrador:
        bot.send_message( administrador, "El usuario con ID: " + str(cid) + " ha intentado utilizar el comando para enviar difundidos")
    else:
        for ID in usuarios:
            try:
                bot.send_message( int(ID), m.text[4:])
            except:
                bot.send_message( administrador, "Error enviando mensaje a: " + ID)
            else:
                bot.send_message( administrador, "Éxito enviando mensaje a: " + ID)
#############################################
#API1
@bot.message_handler(commands=['cryptos'])
def command_crypto(m):
    cid = m.chat.id
    
    api = os.environ['keyC']
    payload = {'key': api}
    r=requests.get("https://www.worldcoinindex.com/apiservice/json",params=payload)
    doc = r.json()
    markets=doc['Markets']
    moneda='Bitcoin'
    
    text = m.text
    texts = text.split(' ')  
    
    for i in  markets:
        if len(texts) == 2:
            if i['Name'] == texts[1].capitalize():
                dolar=i['Price_usd']
                euro=i['Price_eur']
                volumen=i['Volume_24h']
                frase='%s tiene un precio de: 💵 %.2f USD, 💶 %.2f EUR, con un volumen 💸 de %d en las ultimas 24h' % (i['Name'],dolar,euro,volumen)
                bot.send_message( cid, frase)
        else:
            if i['Name'] == moneda.capitalize():
                dolar=i['Price_usd']
                euro=i['Price_eur']
                volumen=i['Volume_24h']
                frase='%s tiene un precio de: 💵 %d USD, 💶 %d EUR, con un volumen 💸 de %d en las ultimas 24h' % (i['Name'],dolar,euro,volumen)
                bot.send_message( cid, frase)
#API INLINE
@bot.inline_handler(lambda query: query.query == 'cryptos')
def query_text(inline_query):
    try:
        
        api = os.environ['keyC']
        payload = {'key': api}
        r=requests.get("https://www.worldcoinindex.com/apiservice/json",params=payload)
        doc = r.json()
        markets=doc['Markets']
        moneda1='Bitcoin'
        moneda2='Ethereum'
        for i in  markets:
            if i['Name'] == moneda1:
                nombre1=i['Name']
                dolar1=i['Price_usd']
                euro1=i['Price_eur']
                volumen1=i['Volume_24h']
                frase1='%s tiene un precio de: 💵 %d USD, 💶 %d EUR, con un volumen 💸 de %d en las ultimas 24h' % (nombre1,dolar1,euro1,volumen1)
            elif i['Name'] == moneda2:
                nombre2=i['Name']
                dolar2=i['Price_usd']
                euro2=i['Price_eur']
                volumen2=i['Volume_24h']
                frase2='%s tiene un precio de: 💵 %d USD, 💶 %d EUR, con un volumen 💸 de %d en las ultimas 24h' % (nombre2,dolar2,euro2,volumen2)

        r = types.InlineQueryResultArticle('1', 'cryptos Bitcoin', types.InputTextMessageContent(frase1))
        r2 = types.InlineQueryResultArticle('2', 'cryptos Etherum', types.InputTextMessageContent(frase2))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)
#API2
@bot.message_handler(commands=['top5'])
def command_crypto2(m):
    cid = m.chat.id
    
    api = os.environ['keyC']
    payload = {'key': api, 'label': 'ethbtc-ltcbtc-btcbtc-xmrbtc-xrpbtc', 'fiat': 'eur'}
    r=requests.get("https://www.worldcoinindex.com/apiservice/ticker",params=payload)
    doc = r.json()
    markets=doc['Markets']
    
    for i in markets:
        nombre=i['Name']
        precio=i['Price']
        volumen=i['Volume_24h']
        frase='%s tiene un precio de: 💶 %.2f EUR, con un volumen 💸 de %d en las ultimas 24h' % (nombre,precio,volumen)
        bot.send_message( cid, frase)

#############################################
#Peticiones
bot.polling(none_stop=True)
