import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import ShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score


def display_prediction(df) : 
        # Création d'un set avec les colonnes LSTAT, RM
    X = pd.DataFrame(np.c_[df[['artiste_popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness']]], 
                    columns = ['artiste_popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness'])

    Y = df['popularity']

    # ShuffleSplit est utilisée pour la validation croisée
    cv = ShuffleSplit(3, test_size = 0.2)
    results = cross_val_score(LinearRegression(), X, Y, cv = cv)

    print('Accuracy :', results.mean() * 100.0, '%')
    print('\nCross-Val Details :', results)

    

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.3, random_state=101)
    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)

    
    scaler = StandardScaler()

    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)    
    linear_model = LinearRegression()
    linear_model.fit(X_train, Y_train)

    
    # évaluation du modèle pour l'ensemble d'entraînement
    y_train_predict = linear_model.predict(X_train)
    rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
    r2 = r2_score(Y_train, y_train_predict)
    print("La performance du Modèle pour le set de Training")
    print("------------------------------------------------")
    print("l'erreur RMSE esst {}".format(rmse))
    print('le score R2 est {}'.format(r2))
    print("\n")
    # évaluation du modèle pour le set de tesst
    y_test_predict = linear_model.predict(X_test)
    # racine carrée de l'erreur quadratique moyenne du modèle
    rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
    # score R carré du modèle
    r2 = r2_score(Y_test, y_test_predict)
    print("La performance du Modèle pour le set de Test")
    print("--------------------------------------------")
    print("l'erreur RMSE est {}".format(rmse))
    print('le score R2 score est {}'.format(r2))
    r2_text = 'le score R2 score est {}'.format(r2)
    rmse_text = "l'erreur RMSE est {}".format(rmse)
    fig, ax = plt.subplots()
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.35, 0.1, r2_text, transform=ax.transAxes, fontsize=10,verticalalignment='top', bbox=props)
    ax.text(0.35, 0.05, rmse_text, transform=ax.transAxes, fontsize=8,verticalalignment='top', bbox=props)

    sns.scatterplot(x=Y_test, y=y_test_predict)
    plt.show()
    