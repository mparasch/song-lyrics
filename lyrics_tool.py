# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:07:26 2020

@author: Matt
"""

import tkinter as tk
import requests

root = tk.Tk()
root.title('Song Lyrics')
root.geometry("800x600")

music_photo = tk.PhotoImage(file = 'background.png')
tk.Label(root, image = music_photo).place(relwidth = 1, relheight = 1, x = 0, y = 0)


# =============================================================================
# Artist entry code :
# =============================================================================
artist_frame = tk.Frame(root, bg = '#a8babf')
artist_frame.place(anchor = 'w', relwidth = 0.4, relheight = 0.05, relx = 0.2, rely = 0.1)

tk.Label(artist_frame, text = "Artist: ", bg = '#a8babf', relief = 'raised', font=('Calibri', 12)).place(anchor = 'w', relheight = 1, relwidth = 0.3, relx = 0, rely = 0.5)

artist_entry = tk.Entry(artist_frame, bg = 'white', font = ('Calibri', 12))
artist_entry.place(anchor = 'w', relwidth = 0.69, relheight = 0.9, relx = 0.305, rely = 0.5)


# =============================================================================
# Song entry code
# =============================================================================
song_frame = tk.Frame(root, bg = '#a8babf')
song_frame.place(anchor = 'w', relwidth = 0.4, relheight = 0.05, relx = 0.2, rely = 0.2)
tk.Label(song_frame, text = "Song Name: ", bg = '#a8babf', relief = 'raised', font = ('Calibri', 12)).place(anchor = 'w', relheight = 1, relwidth = 0.3, relx = 0, rely = 0.5)

song_list = ['Search an Artist to populate dropdown']

selection = tk.StringVar(root)

song_selection = tk.OptionMenu(song_frame, selection, *song_list)
song_selection.place(anchor = 'w', relwidth = 0.69, relheight = 0.9, relx = 0.305, rely = 0.5)

# =============================================================================
# Populate Dropdown Button
# =============================================================================
pop_button_frame = tk.Frame(root, bg = '#a8babf')
pop_button_frame.place(anchor = 'e', relwidth = 0.15, relheight = 0.075, relx = 0.8, rely = 0.1)

pop_button = tk.Button(pop_button_frame, text = 'Search Artist', bg = '#a8babf', relief = 'raised', bd = 6, font = ('Calibri', 12), command = lambda: get_songList(artist_entry.get()))
pop_button.place(anchor = 'center', relwidth = 1, relheight = 1, relx = 0.5, rely = 0.5)

# =============================================================================
# Get Lyrics Button
# =============================================================================
button_frame = tk.Frame(root, bg = '#a8babf')
button_frame.place(anchor = 'e', relwidth = 0.15, relheight = 0.075, relx = 0.8, rely = 0.2)

submit_button = tk.Button(button_frame, text = 'Get Lyrics', bg = '#a8babf', relief = 'raised', bd = 6, font = ('Calibri', 12), command = lambda: get_lyrics(artist_entry.get(), selection.get()))
submit_button.place(anchor = 'center', relwidth = 1, relheight = 1, relx = 0.5, rely = 0.5)


# =============================================================================
# Lyrics Output
# =============================================================================
lower_frame = tk.Canvas(root, bg = 'white', relief = 'sunken', bd = 5)
lower_frame.place(anchor = 'n', relwidth = 0.6, relheight = 0.7, relx = 0.5, rely = 0.25)

sbar = tk.Scrollbar()
sbar.pack(side = tk.RIGHT, fill = 'y')

song_list = []
# =============================================================================
# Button Functions
# =============================================================================
def get_lyrics(artist, song):

    txt_box = tk.Text(lower_frame, font = ("Calibri", 11), padx = 25, yscrollcommand = sbar.set, relief = 'sunken', bd = 5)
    txt_box.place(relheight = 1, relwidth = 1)
    try:
        response = requests.get('https://api.lyrics.ovh/v1/' + str(artist) + '/' + str(song))
        lyrics_output = response.json()['lyrics']
        txt_box.insert(tk.END, lyrics_output)
    except:
        txt_box.insert(tk.END, 'Sorry! We do not have the lyrics to the song you selected.')
        
    sbar.config(command = txt_box.yview)
    
def get_songList(artist):
    song_list = []
    try:
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    
        querystring = {"q":str(artist)}
        
        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "0f5b92c46emsha4aa56a91371d79p19cf2cjsn7ff9c3078d0f"
            }
    
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        artist_id = str(response['data'][0]['artist']['id'])
        song_response = requests.get('https://api.deezer.com/artist/' + artist_id + '/top?limit=1000').json()
    
        for i in range(song_response['total']):
            song_list.append(song_response['data'][i]['title_short'].title())
        
        song_list = list(set(song_list))
        song_list.sort()
        song_selection = tk.OptionMenu(song_frame, selection, *song_list)
        song_selection.place(anchor = 'w', relwidth = 0.69, relheight = 0.9, relx = 0.305, rely = 0.5)
        try:
            selection.set(song_list[0])
        except:
            pass
    except:
        error = tk.Tk()
        error.geometry("300x75")
        error.title('Arist Not Found')
        
        def close():
            error.destroy()
        
        msg = tk.Label(error, text = 'The artist you searched was not found')
        msg.pack(anchor = 'center')
        
        ok = tk.Button(error, text = 'OK', command = close)
        ok.pack(anchor = 'center')
        
        error.mainloop()

root.mainloop()