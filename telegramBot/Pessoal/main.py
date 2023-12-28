from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import telebot

bot = telebot.TeleBot("")

escolha = False

def enviar(mensagem,id):
    bot.send_message(id,mensagem)

def rN(msge,cap):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://centralnovel.com/keyboard-immortal-capitulo-{cap}/")
    








def verificar(msg):
    if "/comandos" in msg.text:
        comandos(msg)
    if "/Novels" in msg.text:
        bot.reply_to(msg,"Fala aí patrão, quer qual novel?\n   1- Keyboard Immortal")
        ki = True
    if ki:
        bot.reply_to(msg,"Me diz aí, qual o capítulo que tu quer que eu pegue?")
        ki = False
        ki1 = True
    if ki1:
        novel1 = False
        rN(msg,msg.text)
                     
@bot.message_handler(func=verificar)
def comandos(msg):
    bot.reply_to(msg,"| Comandos:\n    - /Novels")
    




bot.polling()
