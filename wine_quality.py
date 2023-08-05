import pandas as pd
import plotly.express as px

wine_df = pd.read_excel('WineQuality.xlsx')
wine_df = wine_df.rename(columns={'Unnamed: 0':'ID'})

for coluna in wine_df.columns:
    grafic = px.histogram(wine_df, x = coluna, color = 'quality')
    grafic.show()

#Média inicial: 5.812

#Possiveis causas
#1.'alcohol' maior ou igual a 9.880
#2.'volatile acidity' menor ou igual a 0.314
#3.'citric acid' entre 0.24 e 0.42
#4.'residual sugar' menor que 14

wine_df = wine_df[wine_df['alcohol'] >= 10.92]
wine_df = wine_df[(wine_df['volatile acidity'] <= 0.424) & (wine_df['volatile acidity'] >= 0.145)]
wine_df = wine_df[(wine_df['fixed acidity'] <= 7.4) & (wine_df['fixed acidity'] >= 6.6)]
wine_df = wine_df[(wine_df['citric acid'] >= 0.240) & (wine_df['citric acid'] <= 0.360)]
wine_df = wine_df[wine_df['residual sugar'] <= 6.190]
wine_df = wine_df[wine_df['chlorides'] <= 0.034]
wine_df = wine_df[wine_df['density'] <= 0.992849]
wine_df = wine_df[wine_df['total sulfur dioxide'] <= 173.90]
wine_df = wine_df[(wine_df['pH'] >= 2.89) & (wine_df['pH'] <= 3.54)]
wine_df = wine_df[(wine_df['sulphates'] >= 0.36) & (wine_df['sulphates'] <= 0.9)]

meane = wine_df['quality'].mean()
wine_df.info()
print(meane)

