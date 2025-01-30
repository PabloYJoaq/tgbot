import os

import telebot, requests, string, random


BOT_TOKEN = "6129933648:AAECuYKOxG4HPpphh38q64y2gJ4zDkQL2Mo"

emailo=[]
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['gen_mail','genmail'])
def gen(message):
    fetchmail=requests.Session()
    dom=fetchmail.get("https://inboxes.com/api/v2/domain").json()
    email=''.join(random.choices("abcdefghijklmopqrstuvwxyz",k=7))+"%s@%s"%(random.randint(1,9999),dom['domains'][random.randint(0,18)]['qdn'])
    print(email)
    if len(emailo) != 1:
        emailo.clear()
        emailo.append(email)
    else:
        emailo.append(email)
    bot.reply_to(message,"Your Email: %s"%(email))
@bot.message_handler(commands=['getmessage'])
def getmsg(message):
    msg=requests.get("https://inboxes.com/api/v2/inbox/%s"%(emailo[0])).json()
    bot.reply_to(message,"email: %s\nmail: %s"%(emailo[0],str(msg).replace(",","\n")))
bot.infinity_polling()
