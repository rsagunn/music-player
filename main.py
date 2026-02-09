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
    song_list.delete(0, tk.END)

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


            playlist.append({
                "title": title,
                "artist": artist,
                "path": path
            })

            song_list.insert(tk.END, f"{title} - {artist}")

    
    if playlist: # if songs found
        print("Loaded songs:") 
        for song in playlist: # print title and artist
            print(f"{song['title']} - {song['artist']}") # print title and artist
    else:
        print("No MP3 files found") 


def play_song(): # define play song
    global paused

    if not playlist: #if no playlist
        return

    song_path = playlist[current_song]["path"] # get song path
    pygame.mixer.music.load(song_path) # load song
    pygame.mixer.music.play() # play song
    paused = False # set paused to false

    now_playing.config(
        text=f"Now Playing: {playlist[current_song]['title']} - {playlist[current_song]['artist']}" # now playing label
    )

    song_list.selection_clear(0, tk.END)
    song_list.selection_set(current_song) # select current song


#select songs and show all controls

def select_song(event): # define select song
    global current_song 

    selection = song_list.curselection() # get selected list
    if not selection: # if no selection
        return

    current_song = selection[0] # set current song



def pause_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True





def set_volume(value): 
    volume = float(value) / 100  # convert 0–100 to 0.0–1.0
    pygame.mixer.music.set_volume(volume) # set volume




#add a fullscreen feature

# window
window = tk.Tk() # create the window
window.title("Nightwave") # window title
window.geometry("500x500") # size
window.configure(bg="#363636") # background color


tk.Button(window, text="Load Folder", command=load_folder).pack(side=tk.TOP, padx=10, pady=5)   


now_playing = tk.Label(
    window,
    text="Now Playing: None",
    bg="#363636",
    fg="white"
)
now_playing.pack(pady=5)


song_list = tk.Listbox(
    window,
    width=55,
    height=10,
    bg="#222222",
    fg="white",
    selectbackground="#555555"
)

song_list.pack(pady=10)

song_list.bind("<<ListboxSelect>>", select_song)

controls = tk.Frame(window, bg="#363636")
controls.pack(pady=10)


volume_label = tk.Label(
    window,
    text="Volume",
    bg="#363636",
    fg="white"
)
volume_label.pack() # pack label

volume_slider = tk.Scale(
    window,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=set_volume, # set volume
    bg="#363636",
    fg="white",
    highlightthickness=0 
)
volume_slider.set(50)  # default volume = 50%
volume_slider.pack(pady=5) # slider



tk.Button(controls, text="▶ Play", command=play_song).grid(row=0, column=1, padx=5)
tk.Button(controls, text="⏸ Pause/Unpause", command=pause_song).grid(row=0, column=2, padx=5)


window.mainloop() 