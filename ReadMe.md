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

### Step 4: Generating graphics to get some insights 
As we could see, a mean of 5.812 it's very low about quality. So, the challenge is reach out 7.000, at least. To help us with this challenge, some graphics were generated, relating the quality (x axis) in funtion of the chemical parameters (y Axis). Some insights could be get:

**1. Quality x Alcohol:** The bests types of wine have more alcohol in its composition compared with the worsts ones. Analysing deeply the graphic, values higher than 10.920 can be interesting.

**2. Quality x Volatile Acidity:** The bests types of wine have a volatile acidity between 0.150 and 0.450 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 0.280 and 0.370 can be interesting.

**3. Quality x Fixed Acidity:** The bests types of wine have a volatile acidity between 6.000 and 7.500 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 6.600 and 7.300 can be interesting.

**4. Quality x Citric Acid:** The bests types of wine have a volatile acidity between 0.250 and 0.400 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 0.280 and 0.320 can be interesting.










    
    


