import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import *


def display_something(data, xlabel, table_column ) :

    song_popularity = []
    second_paramater = []
    for row in data:
        second_paramater.append(row[table_column])
        song_popularity.append(row[2])


    root = tkinter.Tk()
    root.wm_title("Etudes graphiques")
    #creer la frame principale
    frame = tkinter.Frame(root, bg='#4065A4')
    frame.pack(expand=tkinter.YES)
    #creer une sous boite
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot()
    ax.scatter(second_paramater,song_popularity)
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel("popularity")
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


    dropdown = tkinter.Menubutton( root, text = "Choisir en x")
    choice = tkinter.Menu(dropdown, tearoff=0)
    choice.add_command(label="popularity artist", command= lambda:[root.destroy(), display_something(data, 'popu artist', table_column=26)])
    choice.add_command(label="nb de followers", command= lambda:[root.destroy(),display_something(data, 'nb de followers', table_column=23)])
    choice.add_command(label="durée", command= lambda:[root.destroy(),display_something(data, 'durée en ms', table_column=3)])

    dropdown["menu"] = choice
    dropdown.pack(side=tkinter.BOTTOM)


    tkinter.mainloop()