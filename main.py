playlist = [] # list of songs
current_song = 0 # info of current song
paused = False # paused

import os
import tkinter as tk
from tkinter import filedialog
import time
import pygame
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
pygame.init()
pygame.mixer.init()

os.listdir

#scan for mp3 files and metadata

def load_folder(): #func load folder
    global playlist, current_song # global vars

    folder = filedialog.askdirectory() # opens folder selector
    if folder == "": # if no folder selected
        return # go back
    

    playlist = [] 
    current_song = 0

    for file in os.listdir(folder): # scan files in folder
        if file.lower().endswith(".mp3"): # lower case and check if end with .mp3
            path = os.path.join(folder, file) # full path

            try:
                audio = MP3(path, ID3=EasyID3) # get mp3 metadata
                title = audio.get("title", [file])[0] # title
                artist = audio.get("artist", ["Unknown Artist"])[0] # artist
            except:
                title = file # if no metadata included
                artist = "Unknown Artist" # use this name


            song = {
                "title": title,
                "artist": artist,
                "path": path
            }

            playlist.append(song)

    
    if playlist: # if songs found
        print("Loaded songs:") 
        for song in playlist: # print title and artist
            print(f"{song['title']} - {song['artist']}") # print title and artist
    else:
        print("No MP3 files found")






#display mp3 files in a list with metadata




#select songs and show all controls





#keep playing songs in a loop until user exits




#add a fullscreen feature

# window
window = tk.Tk() # create the window
window.title("Nightwave") # window title
window.geometry("400x300") # size
window.configure(bg="#363636") # background color


tk.Button(window, text="Load Folder", command=load_folder).pack(pady=5)   


window.mainloop() 