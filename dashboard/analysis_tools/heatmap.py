import seaborn as sns
import matplotlib.pyplot as plt

def open_heatmap(df) :    
    df = df.drop_duplicates()
    plt.figure(figsize=(16, 6))
    df.corr()
    heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
    plt.show()

