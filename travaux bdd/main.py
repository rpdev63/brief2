import helpers.data_functions as dfun

def main(): 
    
    #Récupération des données
    database = r"..\Ressources\Sources_data.db"
    conn = dfun.create_connection(database)

    print("Création de tables d'association")
    #décommenter les lignes ci-dessous pour construire des tableaux associatifs puis préciser le nombre de chansons retenus
    dfun.associate_artists_songs(conn, 1000)
    dfun.associate_artists_genres(conn,1000)

    data = dfun.get_full_data(conn,1000)
    print(data)

if __name__ == "__main__":
    main()
