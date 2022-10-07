from tkinter import *
import analysis_tools.heatmap as hm
import analysis_tools.histogrammes as his
import analysis_tools.regression as reg
import analysis_tools.regmul as regmul

import pandas as pd

#df_origine = pd.read_csv(r"../Ressources/chansons.csv")
df_100000 = pd.read_csv(r"../csv/top100000.csv")


def create_frame1(window) :    
    frame = Frame(window, background="#365BE3")
    label_title = Label(frame, text='ANGELIA', font=("Arial",35), bg='#365BE3', fg="#FFF")  # pour background, foreground
    label_title.pack(expand=YES)       
    label_title2 = Label(frame, text='L\'IA qui prédit le top 50 !', font=("Courrier",20), bg='#365BE3', fg="#F5FF27", pady=30)  # pour background, foreground
    label_title2.pack(expand=YES)       
    return frame

def create_frame2(window) :
    frame = Frame(window, background="#365BE3")
    label_title = Label(frame, text='Choix de l\'analyse', font=("Courrier",35), bg='#365BE3', fg="#F5FF27", pady=30)  # pour background, foreground
    label_title.pack(expand=YES, side=TOP) 
    button1 = Button(frame, text="Graphiques de répartition", font=("Courrier",18), fg="#FFF", bg="#000",  pady=8,  command=lambda:[his.display_something(df_100000, "popularity", "totalité")])  
    button1.pack(fill=X, pady=8)

    button2 = Button(frame, text="Matrice de corrélation", font=("Courrier",18), fg="#FFF", bg="#000", highlightcolor="#F5FF27",pady=8, command=lambda:[hm.open_heatmap(df_100000)])
    button2.pack(fill=X,  pady=8)
    button4 = Button(frame, text="Régressions linéaire", font=("Courrier",18), fg="#FFF", bg="#000", highlightcolor="#F5FF27",pady=8, command=lambda:[reg.display_something(df_100000, "artiste_popularity")] )
    button4.pack(fill=X,  pady=8)  
    button3 = Button(frame, text="Prédiction par reg. lin. multiples", font=("Courrier",18), fg="#FFF", bg="#000",highlightcolor="#F5FF27", pady=8, command=lambda:[regmul.display_prediction(df_100000)])
    button3.pack(fill=X,  pady=8)
    button5 = Button(frame, text="Prédiction par arbre de décision", font=("Courrier",18), fg="#FFF", bg="#000",highlightcolor="#F5FF27", pady=8, command=lambda:[])
    button5.pack(fill=X,  pady=8)
    
    return frame

def create_frame3(window) :
    frame = Frame(window, background="#365BE3")
    label_title = Label(frame, text='Ils ont essayés de faire une IA : ', font=("Courrier",25), bg='#365BE3', fg="#F5FF27", pady=30)  # pour background, foreground
    label_title.pack(expand=YES, side=TOP)     
    #ajouter un second texte
    label_subtitle1 = Label(frame, text='Brice Mulot', font=("Times New Roman",22),  bg='#365BE3', fg="#FFF", pady=40)
    label_subtitle1.pack(expand=YES)   
    label_subtitle2 = Label(frame, text='Dylan Reichart', font=("Times New Roman",22), bg='#365BE3', fg="#FFF", pady=40)  # pour background, foreground
    label_subtitle2.pack(expand=YES)   
    label_subtitle3 = Label(frame, text='Elida Vellayoudom', font=("Times New Roman",22), bg='#365BE3', fg="#FFF", pady=40)  # pour background, foreground
    label_subtitle3.pack(expand=YES)   
    label_subtitle4 = Label(frame, text='Rémi Prince', font=("Times New Roman",22), bg='#365BE3', fg="#FFF", pady=40)  # pour background, foreground
    label_subtitle4.pack(expand=YES)   
    return frame


def main() :    
    #créer une première fenêtre
    window = Tk()
    #personnaliser 
    window.title("IA pour trouver une top chanson")
    window.minsize(800, 600)
    window.geometry("1024x768")
    #window.resizable(width=False, height=False)
    window.iconphoto(False, PhotoImage(file='angelia.png'))
    window.config(background='#365BE3')    
    frame1 = create_frame1(window)
    frame2 = create_frame2(window)
    frame3 = create_frame3(window)
    #creation d'une barre de menu
    menu_bar = Menu(window)
    #creer un premier menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Accueil", command=lambda:[canvas.pack(expand=YES), frame1.pack(), frame2.pack_forget(), frame3.pack_forget()])
    file_menu.add_command(label="Analyses graphiques", command=lambda:[canvas.pack_forget(), frame2.pack(), frame1.pack_forget(), frame3.pack_forget()])    
    file_menu.add_command(label="Crédits", command=lambda:[canvas.pack_forget(), frame3.pack(), frame1.pack_forget(), frame2.pack_forget()])
    file_menu.add_command(label="Quitter", command=lambda:[window.quit()])
    menu_bar.add_cascade(label="Menu", menu=file_menu)
    #ajouter la menu bar
    window.config(menu=menu_bar)
    #creation d'image
    width = 750
    height = 538
    canvas = Canvas(window, width=width, height=height, bg='#365BE3', bd=0, highlightthickness=0) #bd et highlightthickness pour enlever les bordures
    image = PhotoImage(file='angelia.png').zoom(12).subsample(15)  
    canvas.create_image(width/2, height/2,image=image)
    canvas.pack(expand=YES)
    frame1.pack()
    window.mainloop()
    

if __name__ == "__main__":
    main()





