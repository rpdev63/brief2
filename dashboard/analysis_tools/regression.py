
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def display_something(df, xlabel ) :
    #creation de la fenêtre
    root = tkinter.Tk()
    root.wm_title("Régression Linéaire Simple")    
    fig = Figure(figsize=(6, 4), dpi=100)

    #calculs régression linéaire
    Xi = df['popularity']
    yi = df[xlabel]
    m = Xi.count()
    X = (Xi - min(Xi))/(max(Xi)-min(Xi))
    y = (yi - min(yi))/(max(yi)-min(yi))
    X = (X - np.mean(X)) / np.std(X)
    y = (y - np.mean(y)) / np.std(y)
    X = X.to_numpy()
    y = y.to_numpy()
    X = X.reshape((m,1))
    regression_model = LinearRegression()
    regression_model.fit(X, y)
    # Predict
    y_predicted = regression_model.predict(X)
    # model evaluation
    rmse = mean_squared_error(y, y_predicted)
    r2 = r2_score(y, y_predicted)
    
    
    #title
    label_title = tkinter.Label(root, text="Régression linéaire simple", font=("Courrier",15), bg='#aaa', fg="#FFF")  # pour background, foreground
    label_title.pack(expand=tkinter.YES, side=tkinter.TOP)   #side = LEFT, BOTTOM... si besoin
     

    #graphique
    ax = fig.add_subplot()
    ax.scatter(X,y,s=10)
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel("popularity")
    ax.plot(X, y_predicted, color='r')
    r2_text = 'Score R2 = {}'.format(r2)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.5, 0.1, r2_text, transform=ax.transAxes, fontsize=10,verticalalignment='top', bbox=props)
    

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

    #dropdown, changer l'axe des abcisses
    dropdown = tkinter.Menubutton( root, text = "Choisir en x")
    choice = tkinter.Menu(dropdown, tearoff=0)
    choice.add_command(label="artiste_popularity", command= lambda:[root.destroy(), display_something(df, 'artiste_popularity')])
    choice.add_command(label="song_danceability", command= lambda:[root.destroy(), display_something(df, 'song_danceability')])
    choice.add_command(label="artistes_followers", command= lambda:[root.destroy(),display_something(df, 'artistes_followers')])
    choice.add_command(label="explicit", command= lambda:[root.destroy(),display_something(df, 'explicit')])
    choice.add_command(label="genre_energy", command= lambda:[root.destroy(),display_something(df, 'genre_energy')])
    choice.add_command(label="genre_popularity", command= lambda:[root.destroy(),display_something(df, 'genre_popularity')])
    choice.add_command(label="genre_speechiness", command= lambda:[root.destroy(),display_something(df, 'genre_speechiness')])
    choice.add_command(label="genre_instrumentalness", command= lambda:[root.destroy(),display_something(df, 'genre_instrumentalness')])
    choice.add_command(label="genre_danceability", command= lambda:[root.destroy(),display_something(df, 'genre_danceability')])
    choice.add_command(label="song_acousticness", command= lambda:[root.destroy(),display_something(df, 'song_acousticness')])
    choice.add_command(label="song_speechiness", command= lambda:[root.destroy(),display_something(df, 'song_speechiness')])
    choice.add_command(label="song_loudness", command= lambda:[root.destroy(),display_something(df, 'song_loudness')])
    dropdown["menu"] = choice
    dropdown.pack(side=tkinter.BOTTOM)

    tkinter.mainloop()


