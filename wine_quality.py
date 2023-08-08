import pandas as pd
import seaborn as sns
import plotly.express as px

#Importing the dataset about the wine quality
wine_df = pd.read_excel('WineQuality.xlsx')

#Dataset informations resume
wine_df.info()

#Renaming the 'ID' column and dropping the type column
wine_df = wine_df.rename(columns={'Unnamed: 0':'ID'})
wine_df = wine_df.drop(['Type'], axis = 1)

#Calculating the wine quality's initial mean
initial_mean = wine_df['quality'].mean()
print(f"Initialy, the mean of the wine quality is {initial_mean :.3f}")

#Checking if there's any correlation among columns using Pearson's correlation
correlation = wine_df.corr()
sns.heatmap(correlation, annot = True, fmt = ".1f", vmax = 1, vmin = -1)

#Generating histogram graphic's for each column in funtion of the quality
for coluna in wine_df.columns:
    grafic = px.histogram(wine_df, x = coluna, color = 'quality')
    grafic.show()

#Setting some chemical parameters based on graphics above and Pearson's correlation
wine_df = wine_df[wine_df['alcohol'] >= 10.920]
wine_df = wine_df[(wine_df['volatile acidity'] >= 0.280) & (wine_df['volatile acidity'] <= 0.370)]
wine_df = wine_df[(wine_df['fixed acidity'] >= 6.600) & (wine_df['fixed acidity'] <= 7.300)]
wine_df = wine_df[(wine_df['citric acid'] >= 0.280) & (wine_df['citric acid'] <= 0.320)]
wine_df = wine_df[(wine_df['residual sugar'] >= 2.300) & (wine_df['residual sugar'] <= 6.200)]
wine_df = wine_df[wine_df['chlorides'] <= 0.034]
wine_df = wine_df[(wine_df['density'] >= 0.989) & (wine_df['density'] <= 0.992)]
wine_df = wine_df[(wine_df['total sulfur dioxide'] >= 80) & (wine_df['total sulfur dioxide'] <= 129)]
wine_df = wine_df[(wine_df['pH'] >= 2.890) & (wine_df['pH'] <= 3.540)]
wine_df = wine_df[(wine_df['sulphates'] >= 0.360) & (wine_df['sulphates'] <= 0.900)]
wine_df = wine_df[(wine_df['free sulfur dioxide'] <= 64) & (wine_df['total sulfur dioxide'] >= 20)]

#Calculating the mean after filtering 
new_mean_quality = wine_df['quality'].mean()

#Printing new mean
print(f"After setting some chemical parameters, the new mean is {new_mean_quality :.3f}")

