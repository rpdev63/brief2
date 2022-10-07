
import helpers.data_functions as dfun

def main(): 

    #Récupération des données
    database = r"C:\Users\utilisateur\code\angelia\brief2\Ressources\Sources_data.db"
    conn = dfun.create_connection(database)   
    
    #décommenter les lignes ci-dessous pour construire des tableaux associatifs puis préciser le nombre de chansons retenus
    #df.associate_artists_songs(conn, 100000)  
    #df.associate_artists_genres(conn,100000)

    data = dfun.get_full_data(conn,3000)

if __name__ == "__main__":
    main()
