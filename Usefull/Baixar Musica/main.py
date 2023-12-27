from pytube import Search
from pytube import YouTube
import os
from moviepy.editor import *
import string

musicas = []
ids = []
nmusicas = []
contador = 1

import string

def sanitize(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)

try:
    with open('lista.txt','r', encoding='utf-8') as lista:
        for linha in lista:
            nome = linha.strip()
            musicas.append(nome)
except FileNotFoundError:
    print("Arquivo não encontrado")

for i in range(len(musicas)):
    busca = Search(musicas[i])
    ids.append(busca.results[0].video_id)

for i in range(len(ids)):
    ObjetoYT = YouTube('https://www.youtube.com/watch?v='+ids[i])
    titulo = sanitize(ObjetoYT.title)
    stream = ObjetoYT.streams.get_by_itag(251)
    nmusicas.append(str(contador)+' - '+titulo+'.webm')
    stream.download(output_path='output/',filename=nmusicas[i])
    contador +=1

    vaudio = AudioFileClip('output/'+nmusicas[i])
    nomem = nmusicas[i].replace('webm','mp3')
    vaudio.write_audiofile('output/'+nomem)

    os.remove('output/'+nmusicas[i])




