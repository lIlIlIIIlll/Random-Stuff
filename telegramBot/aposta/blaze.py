import requests
import json
import telebot
import time
import random as r

bot = telebot.TeleBot("6977412745:AAHNk3N4tRIvYkq2hPv3FWAZ40k5AsOG-wo")
id = -1001913180272

def blaze(vezes):
    api = "https://blaze-4.com/api/roulette_games/recent"
    verm = 0
    cin = 0
    resp = json.loads(requests.get(api).text)

    if vezes == 3 or vezes == 4:
        resultado = r.randint(1,10)
        if resultado == 10:
            return "branco"
    
    for index, valor in enumerate(resp):
        if index < 2:
            for index, valor in enumerate(resp):
                if index < 3:
                    if valor["color"] == 1:
                        verm += 1
                    elif valor["color"] == 2:
                        cin += 1

                    if verm == 4:
                        return "vermelho"
                    elif cin == 4:
                        return "cinza"
                    elif verm == 3:
                        return "cinza"
                    elif cin == 3:
                        return "vermelho"
                else:
                    cin = 0
                    verm = 0
                    break
            if valor["color"] == 1:
                verm += 1
            elif valor["color"] == 2:
                cin += 1
        break

    if verm > cin:
        return "vermelho"
    elif cin > verm:
        return "cinza"
    elif verm == cin:
        resultado = r.randint(1,2)
        if resultado == 1:
            return "vermelho -b"
        else:
            return "cinza -b"

def enviar(mensagem):
    bot.send_message(id,mensagem)

branco = 0
print(f"Bot Iniciado. Ele está configurado no momento para o chat de ID: {id}\nDeseja mudar o id do chat? [s]n\n")
id = input()
if id == "s" or id == "":
    id = int(input("\nCerto, o ID de chat será trocado, digite o novo ID: "))
else:
    id = -1001913180272
while True:
    resposta = blaze(branco)
    if branco == 4:
        branco = 0
    else:
        branco += 1
    
    if resposta == "vermelho -b":
        enviar("✅ Robô Confirma ✅\n🎯Aposte baixo no 🟥")
    elif resposta == "cinza -b":
        enviar("✅ Robô Confirma ✅\n🎯Aposte baixo no ⬛")
    elif resposta == "vermelho":
        enviar("✅ Robô Confirma ✅\n🎯Aposte no 🟥")
    elif resposta == "cinza":
        enviar("✅ Robô Confirma ✅\n🎯Aposte no ⬛")    
    elif resposta == "branco":
        enviar("✅ Robô Confirma ✅\n🎯Aposte no ⬜") 


    time.sleep(300)