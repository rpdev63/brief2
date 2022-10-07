import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ eate a database connection to the SQLite crdatabase
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def request(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def insert_table_artistes_chansons(conn, id1,id2):
    cur = conn.cursor()
    cur.execute("INSERT INTO artistes_chansons(artiste_id, chanson_id) VALUES(?,?)",(id1,id2,))
    conn.commit()
    return cur.lastrowid

def insert_table_artistes_genres(conn, id,genre_name):
    cur = conn.cursor()
    cur.execute("INSERT INTO artistes_genres(artiste_id, genre_name) VALUES(?,?)",(id,genre_name,))
    conn.commit()
    return cur.lastrowid


def get_top_songs(conn, number):
    cur = conn.cursor()
    cur.execute("SELECT chansons.popularity as cp, artistes.popularity as ap FROM chansons INNER JOIN artistes_chansons ON chanson_id = chansons.id INNER JOIN artistes ON artiste_id = artistes.id ORDER BY chansons.popularity DESC LIMIT ?", (number,))
    return cur.fetchall()

def get_everything_from_top_songs(conn, number):
    cur = conn.cursor()
    cur.execute("SELECT * FROM chansons INNER JOIN artistes_chansons ON chanson_id = chansons.id INNER JOIN artistes ON artistes_chansons.artiste_id = artistes.id  INNER JOIN artistes_genres ON artistes_genres.artiste_id = artistes.id INNER JOIN par_genres_o ON artistes_genres.genre_name = par_genres_o.genres LIMIT ?", (number,))
    return cur.fetchall()

def get_full_data(conn, number):
    cur = conn.cursor()
    print("chargement")
    cur.execute("SELECT chansons.id, chansons.name as song_name, chansons.popularity as popularity, chansons.duration_ms as song_duration_ms, explicit, id_artists, release_date, chansons.danceability as song_danceability, chansons.energy as song_energy, chansons.key as song_key, chansons.loudness as song_loudness, chansons.mode as song_mode, chansons.speechiness as song_speechiness, chansons.acousticness as song_acousticness, chansons.instrumentalness as song_instrumentalness, chansons.liveness as song_liveness, chansons.valence as song_valence, chansons.tempo as song_tempo, time_signature as song_time_signature, artistes.followers as artistes_followers, artistes.genres as artistes_genres, artistes.name as artiste_name, artistes.popularity as artiste_popularity, genre_name, par_genres_o.mode as genre_mode, par_genres_o.acousticness as genre_acousticness, par_genres_o.danceability as genre_danceability, par_genres_o.duration_ms as genre_duration_ms, par_genres_o.energy as genre_energy, par_genres_o.instrumentalness as genre_instrumentalness, par_genres_o.liveness as genre_liveness, par_genres_o.loudness as genre_loudness, par_genres_o.speechiness as genre_speechiness, par_genres_o.tempo as genre_tempo, par_genres_o.valence as genre_valence, par_genres_o.popularity as genre_popularity, par_genres_o.key as genre_key FROM chansons INNER JOIN artistes_chansons ON chanson_id = chansons.id INNER JOIN artistes ON artistes_chansons.artiste_id = artistes.id  INNER JOIN artistes_genres ON artistes_genres.artiste_id = artistes.id INNER JOIN par_genres_o ON artistes_genres.genre_name = par_genres_o.genres LIMIT ?", (number,))
    print("récupération ok")
    return cur.fetchall()

def get_top_artists(conn, number):
    cur = conn.cursor()
    cur.execute("SELECT chansons.popularity as cp, artistes.followers as ap FROM chansons INNER JOIN artistes_chansons ON chanson_id = chansons.id INNER JOIN artistes ON artiste_id = artistes.id ORDER BY artistes.popularity DESC LIMIT ?", (number,))
    return cur.fetchall()

def get_top50_songs(conn) :
    cur = conn.cursor()
    cur.execute("SELECT chansons.id, chansons.name as song_name, chansons.popularity as popularity, chansons.duration_ms as song_duration_ms, explicit, id_artists, release_date, chansons.danceability as song_danceability, chansons.energy as song_energy, chansons.key as song_key, chansons.loudness as song_loudness, chansons.mode as song_mode, chansons.speechiness as song_speechiness, chansons.acousticness as song_acousticness, chansons.instrumentalness as song_instrumentalness, chansons.liveness as song_liveness, chansons.valence as song_valence, chansons.tempo as song_tempo, time_signature as song_time_signature, artistes.followers as artistes_followers, artistes.genres as artistes_genres, artistes.name as artiste_name, artistes.popularity as artiste_popularity, genre_name, par_genres_o.mode as genre_mode, par_genres_o.acousticness as genre_acousticness, par_genres_o.danceability as genre_danceability, par_genres_o.duration_ms as genre_duration_ms, par_genres_o.energy as genre_energy, par_genres_o.instrumentalness as genre_instrumentalness, par_genres_o.liveness as genre_liveness, par_genres_o.loudness as genre_loudness, par_genres_o.speechiness as genre_speechiness, par_genres_o.tempo as genre_tempo, par_genres_o.valence as genre_valence, par_genres_o.popularity as genre_popularity, par_genres_o.key as genre_key FROM chansons INNER JOIN artistes_chansons ON chanson_id = chansons.id INNER JOIN artistes ON artistes_chansons.artiste_id = artistes.id  INNER JOIN artistes_genres ON artistes_genres.artiste_id = artistes.id INNER JOIN par_genres_o ON artistes_genres.genre_name = par_genres_o.genres WHERE chansons.popularity > 89 ORDER BY popularity DESC")
    return cur.fetchall()

def get_ids_artists_songs(conn, number):   
    cur = conn.cursor()
    cur.execute("SELECT id,id_artists FROM chansons ORDER BY popularity DESC LIMIT ?",(number ,))
    return cur.fetchall()

def get_ids_artists_genres(conn, number):   
    cur = conn.cursor()
    cur.execute("SELECT id,genres FROM artistes ORDER BY popularity DESC LIMIT ?",(number ,))
    return cur.fetchall()



def transform_string(str):
    """ transform le texte en tableau """
    characters = "'[] "
    for letter in range(len(characters)) :
        str = str.replace(characters[letter],'')        
    return str.split(',')

def associate_artists_songs(conn, number) :
    request(conn,"DROP TABLE IF EXISTS artistes_chansons")
    request(conn,"CREATE TABLE IF NOT EXISTS artistes_chansons(artiste_id varchar(50) NOT NULL, chanson_id varchar(50) NOT NULL,FOREIGN KEY(artiste_id) REFERENCES artistes(id),FOREIGN KEY(chanson_id) REFERENCES chansons(id), PRIMARY KEY(artiste_id, chanson_id))")
    result = get_ids_artists_songs(conn, number)
    for row in result :
        id_song = row[0]
        id_artists = transform_string(row[1])
        for id_artist in id_artists :
            insert_table_artistes_chansons(conn,id_artist,id_song)
    print("Fin")
    
def associate_artists_genres(conn, number) :
    request(conn,"DROP TABLE IF EXISTS artistes_genres")
    request(conn,"CREATE TABLE IF NOT EXISTS artistes_genres(artiste_id varchar(50) NOT NULL, genre_name varchar(50) NOT NULL,FOREIGN KEY(artiste_id) REFERENCES artistes(id),FOREIGN KEY(genre_name) REFERENCES par_genres_o(genres), PRIMARY KEY(artiste_id, genre_name))")
    result = get_ids_artists_genres(conn, number)
    for row in result :
        id_artists = row[0]
        genres_names = transform_string(row[1])        
        for genre_name in genres_names :
            insert_table_artistes_genres(conn,id_artists,genre_name)
    print("Fin")