import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from tkinter import *

def display_something(df, column_name, title) :

    #creation de la fenêtre
    root = tkinter.Tk()
    root.wm_title("Histogrammes")    
    fig = Figure(figsize=(6, 4), dpi=100)

    #Calculs histogrammes
    data = df[column_name]
    bins=np.arange(min(data), max(data) + 1, 1)


    ax = fig.add_subplot()
    ax.hist(df[column_name], bins)
    ax.set_label(column_name)

    #title
    label_title = Label(root, text=( column_name), font=("Courrier",25), bg='#aaa', fg="#FFF")  # pour background, foreground
    label_title.pack(expand=YES, side=TOP)   #side = LEFT, BOTTOM... si besoin
    
    #canvas tk + toolbar 
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    pack_toolbar=False #will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)    
    toolbar.update()
    canvas.mpl_connect(
        "key_press_event", lambda event: print(f"you pressed {event.key}"))
    canvas.mpl_connect("key_press_event", key_press_handler)
    button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)
    button_quit.pack(side=tkinter.BOTTOM)
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

    current_df = df
    current_parameter = column_name
    #df = pd.read_csv(r"..\Ressources\chansons.csv")
    df2 = pd.read_csv(r"..\csv\top100000.csv")
    df3 = pd.read_csv(r"..\csv\top2500_full.csv")
    df4 = pd.read_csv(r"..\csv\top50.csv")
    
    dropdown = tkinter.Menubutton( root, text = "Modifier l'échantillon")
    choice = tkinter.Menu(dropdown, tearoff=0)
    #choice.add_command(label="totalité", command= lambda:[root.destroy(), display_something(df, current_parameter, "toutes les chansons")])
    choice.add_command(label="top 100000", command= lambda:[root.destroy(), display_something(df2, current_parameter, "top 100000")])
    choice.add_command(label="top 2500", command= lambda:[root.destroy(),display_something(df3, current_parameter, "top 2500")])
    choice.add_command(label="top 50", command= lambda:[root.destroy(),display_something(df4, current_parameter, "top 50")])
    dropdown["menu"] = choice
    dropdown.pack(side=tkinter.BOTTOM)

    dropdown = tkinter.Menubutton( root, text = "Changer de paramètre")
    choice = tkinter.Menu(dropdown, tearoff=0)
    choice.add_command(label="popularity", command= lambda:[root.destroy(), display_something(current_df, 'popularity', label_title)])
    choice.add_command(label="song_duration_ms", command= lambda:[root.destroy(), display_something(current_df, 'song_duration_ms', label_title)])
    choice.add_command(label="explicit", command= lambda:[root.destroy(),display_something(current_df, 'explicit', label_title)])
    choice.add_command(label="song_danceability", command= lambda:[root.destroy(),display_something(current_df, 'song_danceability', label_title)])
    choice.add_command(label="song_energy", command= lambda:[root.destroy(),display_something(current_df, 'song_energy', label_title)])
    choice.add_command(label="song_key", command= lambda:[root.destroy(),display_something(current_df, 'song_key', label_title)])
    choice.add_command(label="song_loudness", command= lambda:[root.destroy(),display_something(current_df, 'song_loudness', label_title)])
    choice.add_command(label="song_mode", command= lambda:[root.destroy(),display_something(current_df, 'song_mode', label_title)])
    choice.add_command(label="song_speechiness", command= lambda:[root.destroy(),display_something(current_df, 'song_speechiness', label_title)])
    choice.add_command(label="song_acousticness", command= lambda:[root.destroy(),display_something(current_df, 'song_acousticness', label_title)])
    choice.add_command(label="song_instrumentalness", command= lambda:[root.destroy(),display_something(current_df, 'song_instrumentalness', label_title)])
    choice.add_command(label="song_liveness", command= lambda:[root.destroy(),display_something(current_df, 'song_liveness', label_title)])
    choice.add_command(label="song_valence", command= lambda:[root.destroy(),display_something(current_df, 'song_valence', label_title)])
    choice.add_command(label="song_tempo", command= lambda:[root.destroy(),display_something(current_df, 'song_tempo', label_title)])
    choice.add_command(label="song_time_signature", command= lambda:[root.destroy(),display_something(current_df, 'song_time_signature', label_title)])
    choice.add_command(label="artistes_followers", command= lambda:[root.destroy(),display_something(current_df, 'artistes_followers', label_title)])
    choice.add_command(label="artiste_popularity", command= lambda:[root.destroy(),display_something(current_df, 'artiste_popularity', label_title)])
    choice.add_command(label="genre_mode", command= lambda:[root.destroy(),display_something(current_df, 'genre_mode', label_title)])
    choice.add_command(label="genre_acousticness", command= lambda:[root.destroy(),display_something(current_df, 'genre_acousticness', label_title)])
    choice.add_command(label="genre_danceability", command= lambda:[root.destroy(),display_something(current_df, 'genre_danceability', label_title)])
    choice.add_command(label="genre_duration_ms", command= lambda:[root.destroy(),display_something(current_df, 'genre_duration_ms', label_title)])
    choice.add_command(label="genre_energy", command= lambda:[root.destroy(),display_something(current_df, 'genre_energy', label_title)])
    choice.add_command(label="genre_instrumentalness", command= lambda:[root.destroy(),display_something(current_df, 'genre_instrumentalness', label_title)])
    choice.add_command(label="genre_liveness", command= lambda:[root.destroy(),display_something(current_df, 'genre_liveness', label_title)])
    choice.add_command(label="genre_loudness", command= lambda:[root.destroy(),display_something(current_df, 'genre_loudness', label_title)])
    choice.add_command(label="genre_speechiness", command= lambda:[root.destroy(),display_something(current_df, 'genre_speechiness', label_title)])
    choice.add_command(label="genre_tempo", command= lambda:[root.destroy(),display_something(current_df, 'genre_tempo', label_title)])
    choice.add_command(label="genre_valence", command= lambda:[root.destroy(),display_something(current_df, 'genre_valence', label_title)])
    choice.add_command(label="genre_popularity", command= lambda:[root.destroy(),display_something(current_df, 'genre_popularity', label_title)])
    choice.add_command(label="genre_key", command= lambda:[root.destroy(),display_something(current_df, 'genre_key', label_title)])
    

    
    dropdown["menu"] = choice
    dropdown.pack(side=tkinter.BOTTOM)

    tkinter.mainloop()

