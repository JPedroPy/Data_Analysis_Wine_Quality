# Wine Quality 🍷
## Analysing Chemical Parameters to Improve the Quality

In this dataset, we have some chemical parameters about types of wine and how they are related with the quality, in a way to set them to improve the quality. The parameters are:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol
- Type

### Step 1: Importing the dataset and getting a short resume of the columns content
When we have a problem to solve involving a data analysis, the first thing to do is importing and reading the dataset. So, we can use the libraby "pandas" to help us with:

    import pandas as pd
    wine_df = pd.read_excel('WineQuality.xlsx')
    wine_df.info()

### Step 2: Cleaning the dataset
In this case, after analysing the resume of informations (columns name, number of rows and data type) I could see that there isn't empty values, but the "ID" columns was named wrongly. So, to fix it:

    wine_df = wine_df.rename(columns{'Unnamed 0':'ID'})

### Step 3: Calculating the initial wine quality's mean
With the dataset informations, the initial quality mean is:

        mean = wine_df['quality'].mean()

The mean in this case is 5.812.
<span style="color:#B81365">Colored text with hexadecimal</span>






    
    


