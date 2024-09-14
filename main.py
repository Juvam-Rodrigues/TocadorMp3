import pygame
from tkinter import *
from threading import *

# Inicializa o mixer do pygame
pygame.mixer.init()

# Função para tocar música
def tocarMusica():
    pygame.mixer.music.load('musica/Nanami.mp3')
    pygame.mixer.music.play()

# Função para parar a música
def pararMusica():
    pygame.mixer.music.stop()

# Função para pausar a música
def pausarMusica():
    pygame.mixer.music.pause()

# Função para continuar a música pausada
def continuarMusica():
    pygame.mixer.music.unpause()

# Thread para tocar a música sem travar a interface
def tocarMusicaThread():
    Thread(target=tocarMusica).start()

#Função de ajustar volume
def ajustarVolume(val):
    volume = int(val) / 100  # Converte o valor do slider (0-100) para o formato do pygame (0.0-1.0)
    pygame.mixer.music.set_volume(volume)


# Configuração da interface tkinter
janela = Tk()
janela.title("Reprodutor MP3 (JuvamVersion)")
janela.geometry("300x300")
janela.configure(bg="#f0f0f0")  # Cor de fundo

# Título
texto = Label(janela, text="Reprodutor MP3",  font=("Helvetica", 16, 'bold'), bg="#a3fec7", fg="#333333") 
texto.grid(column=0, row=0, pady=10, padx=50)

# Botão para tocar a música
botaoTocar = Button(janela, text="Tocar Música", command=tocarMusicaThread)
botaoTocar.grid(column=0, row=1, pady=5)

# Botão para pausar a música
botaoPausar = Button(janela, text="Pausar Música", command=pausarMusica)
botaoPausar.grid(column=0, row=2, pady=5)

# Botão para continuar a música pausada
botaoContinuar = Button(janela, text="Continuar Música", command=continuarMusica)
botaoContinuar.grid(column=0, row=3,  pady=5)

# Botão para parar a música
botaoParar = Button(janela, text="Parar Música", command=pararMusica)
botaoParar.grid(column=0, row=4,  pady=5)

textoVolume = Label(janela, text="Ajustar Volume")
textoVolume.grid(column=0, row=5, pady=5)

volumeSlider = Scale(janela, from_=0, to=100, orient=HORIZONTAL, command=ajustarVolume)
volumeSlider.set(100)  # Volume inicial no máximo
volumeSlider.grid(column= 0, row= 5, pady=8)

# Mantém a janela aberta em loop
janela.mainloop()