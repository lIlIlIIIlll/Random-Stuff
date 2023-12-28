import telebot
import time
import random as r

bot = telebot.TeleBot("")
id = 

def pegarSinal():
    matriz = [["💣","💣","💣","💣","💣"],
              ["💣","💣","💣","💣","💣"],
              ["💣","💣","💣","💣","💣"],
              ["💣","💣","💣","💣","💣"],
              ["💣","💣","💣","💣","💣"]
              ]
    
    for i in range(6):
        linha = r.randint(0,4)
        coluna = r.randint(0,4)
        matriz[linha][coluna] = "💎"
    
    omatriz = ""
    for j in range(5):
        for i in range(5):
            if i == 4:
                omatriz= omatriz+matriz[j][i]
                omatriz = omatriz+"\n"
            else:
                omatriz = omatriz+matriz[j][i]
    
    return omatriz
    
def enviar(mensagem):
    bot.send_message(id,mensagem)


enviar(f"✅ Robô Confirma ✅\n🔁 Tentativas: {r.randint(1,5)}\n\n{pegarSinal()}\n\n🛡️Aposte com: {r.randint(1,3)}")
