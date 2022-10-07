import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def open_heatmap(df) :    
    df = df.drop_duplicates()
    plt.figure(figsize=(16, 6))
    df.corr()
    heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
    plt.show()

# df = pd.read_csv(r"..\..\csv\top100000.csv")
# open_heatmap(df)