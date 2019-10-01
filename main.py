from pytube import YouTube, Playlist
import os
def opsion(x):
    if (x == 0):
        opsi = input("Mau Download apa.? \n1. Single Video\n2. Playlist Video \n3. tutup\n Pilih(1/2/3) : ")
        pilihan(opsi)
        os.system('cls' if os.name =='nt' else 'clear')

def pilihan(y):
    opsi = y
    if (int(opsi)==1):
        link = input("Masukkan Link Single Videonya :")
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download()
        opsion(0)
    elif (int(opsi)==2):
        list = input("Masukkan Link playlist Videonya :")
        yt = Playlist(list)
        yt.download_all()
        opsion(0)
    elif (int(opsi) == 3):
        print("Byeeee")
        exit()
    else:
        print("Pilihan Salah")
        opsion(0)

opsion(0)