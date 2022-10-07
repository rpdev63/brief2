import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


df = pd.read_csv(r'..\csv\top100000.csv')

df = df.drop(["song_name", "artistes_genres", "artiste_name", "genre_name"], axis=1)

df = df[df['popularity'] !=0]
df = df[df['song_duration_ms'] <1000000]
df = df[df['genre_duration_ms'] <1000000]
df = df[df['song_tempo'] <1000000]
df = df[df['genre_tempo'] !=0]

plt.hist(df['popularity'], bins = np.arange(min(df['popularity']), max(df['popularity']) + 1, 1))

plt.show()

 
X = df[['song_duration_ms', 'explicit', 'song_danceability', 'song_energy', 'song_key', 'song_loudness', 'song_mode', 'song_speechiness', 'song_acousticness', 'song_instrumentalness', 'song_liveness', 'song_valence', 'song_tempo', 'song_time_signature', 'artistes_followers', 'artiste_popularity', 'genre_mode', 'genre_acousticness', 'genre_danceability', 'genre_duration_ms', 'genre_energy', 'genre_instrumentalness', 'genre_liveness', 'genre_loudness', 'genre_speechiness', 'genre_tempo','genre_valence', 'genre_popularity', 'genre_key' ]]

#Transformer des valeurs de popularité en données quantitatives
df.loc[df['popularity']  < 90, 'classe'] = 0
df.loc[df['popularity']  >= 90, 'classe'] = 1
Y = df['classe'] 
Y.value_counts()
#la classe 1 
#df[df.classe==1]


#Split du datatest en training set et test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)

#Mise à l'échelle
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Entrainement de la régression logistique au training set
Classifier = LogisticRegression()
Classifier.fit(X_train, Y_train)

#Prédiction des résultats sue le test set
Y_pred = Classifier.predict(X_test)
print(Y_pred)

accuracy = accuracy_score(Y_test, Y_pred)
print(accuracy)
#résultat : 0.999078659449499
#précision du modèle : 99%

ConfusionMatrix = confusion_matrix(Y_test, Y_pred)
print(ConfusionMatrix)
#résultats : [26025     0] 
#            [   24     0]
#26025/(26025+24)=0.99907865449499  -> accuracy
#Interprétation : C'est un bon modèle de prédiction, mais pour les "non Hit" puisque la classe 0 a beaucoup d'échantillon

