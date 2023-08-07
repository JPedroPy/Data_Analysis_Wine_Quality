# Wine Quality 🍷
## Analysing Chemical Parameters to Improve the Quality

In this dataset, we have some chemical parameters about types of wine and how they are related with the quality, in a way to set them to improve the quality. The parameters are:

- Alcohol
- Volatile Acidity
- Fixed Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Density
- Total Sulfur Dioxide
- pH
- Sulphates
- Free Sulfur Dioxide
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

**3. Quality x Fixed Acidity:** The bests types of wine have a fixed acidity between 6.000 and 7.500 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 6.600 and 7.300 can be interesting.

**4. Quality x Citric Acid:** The bests types of wine have a citric acid between 0.250 and 0.400 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 0.280 and 0.320 can be interesting.

**5. Quality x Residual Sugar:** The bests types of wine have a residual sugar between 1.000 and 7.000 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 2.300 and 6.200 can be interesting.

**6. Quality x Chlorides:** The bests types of wine have less chlorides in its composition compared with the worsts ones. Analysing deeply the graphic, values lower than 0.034 can be interesting.

**7. Quality x Density:** The bests types of wine have density between 0.980 and 0.990 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 0.989 and 0.992 can be interesting.

**8. Quality x Total Sulfur Dioxide:** The bests types of wine have total sulfur dioxide between 80 and 150 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 80 and 129 can be interesting.

**9. Quality x pH:** The bests types of wine have pH between 2.850 and 3.600 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 2.890 and 3.540 can be interesting.

**10. Quality x Sulphates:** The bests types of wine have sulphates between 0.300 and 1.000 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 0.360 and 0.900 can be interesting.

**11. Quality x Free Sulfur Dioxide:** The bests types of wine have free sulfur dioxide between 20 and 70 in its composition compared with the worsts ones. Analysing deeply the graphic, values between 20 and 64 can be interesting.

### Step 5: Setting chemical parameters and calculating new mean
Now, taking the bests values for each column and filtering them, the tendency is improve the quality. Checking this up:

        wine_df = wine_df[wine_df['alcohol'] >= 10.920]
        wine_df = wine_df[(wine_df['volatile acidity'] <= 0.370) & (wine_df['volatile acidity'] >= 0.280)]
        wine_df = wine_df[(wine_df['fixed acidity'] <= 7.300) & (wine_df['fixed acidity'] >= 6.600)]
        wine_df = wine_df[(wine_df['citric acid'] >= 0.280) & (wine_df['citric acid'] <= 0.320)]
        wine_df = wine_df[(wine_df['residual sugar'] <= 6.200) & (wine_df['residual sugar'] >= 2.300) ]
        wine_df = wine_df[wine_df['chlorides'] <= 0.034]
        wine_df = wine_df[(wine_df['density'] <= 0.992) & (wine_df['density'] >= 0.989)]
        wine_df = wine_df[(wine_df['total sulfur dioxide'] <= 129) & (wine_df['total sulfur dioxide'] >= 80)]
        wine_df = wine_df[(wine_df['pH'] >= 2.890) & (wine_df['pH'] <= 3.540)]
        wine_df = wine_df[(wine_df['sulphates'] >= 0.360) & (wine_df['sulphates'] <= 0.900)]
        wine_df = wine_df[(wine_df['free sulfur dioxide'] <= 64) & (wine_df['total sulfur dioxide'] >= 20)]

New mean:

        mean_quality = wine_df['quality'].mean()

The new mean is 7.104

### Conclusion
Taking strategical values could improve the wine quality. So, the company who produces the wines should focus on the range of the values for each chemical parameter:

- **Alcohol**: Higher than 10.92
- **Volatile Acidity**: Between 0.280 and 0.370
- **Fixed Acidity**: Between 6.600 and 7.300
- **Citric Acid**: Between 0.280 and 0.370
- **Residual Sugar**: Between 2.300 and 6.200
- **Chlorides**: Lower than 0.034
- **Density**: Between 0.989 and 0.992
- **Total Sulfur Dioxide**: Between 80 and 129
- **pH**: Between 2.890 and 3.540
- **Sulphates**: Between 0.360 and 0.900
- **Free Sulfur Dioxide**: Between 20 and 64

The critical parameter is the density, because it has the shortest range of values (0.989 to 0.992). So, it needs to have the best precision possible to get the range. 
Thus, producing wines with this parameters above, you probably get a good wine to enjoy.







    
    


