from playsound import playsound
from tkinter import *
from threading import *

def tocarMusica():
    playsound("musica/Nanami.mp3")

def tocarMusicaThread():
    Thread(target=tocarMusica).start()

janela = Tk()
janela.title("Reprodutor MP3 (JuvamVersion)")

texto = Label(janela, text="Primeiro teste") #1°janela que faz parte, 2° texto do label
texto.grid(column=0, row=0)

botao = Button(janela, text="Clique aqui para tocar música", command=tocarMusicaThread)
botao.grid(column=0, row=1)


janela.mainloop() #colocamos isso aqui para manter a tela aberta em loop