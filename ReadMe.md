# Wine Quality
## Analysing Chemical Parameters to Improve the Quality

## _Stages of Analysis_
[1. Define the problem](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#1-define-the-problem-%EF%B8%8F-return)

[2. Collect Data](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#2-collect-data-%EF%B8%8F-return)

[3. Data Cleaning and Preprocessing](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#3-data-cleaning-and-preprocessing-%EF%B8%8F-return)

[4. Data Analysis Techniques](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#4-data-analysis-techniques-%EF%B8%8F-return)

[5. Exploratory Data Analysis (EDA) and Interpretation of Results](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#5-exploratory-data-analysis-eda-and-interpretation-of-results-%EF%B8%8F-return)

[6. Conclusion and Recommendations](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#6-conclusion-and-recommendations-%EF%B8%8F-return)

### _1. Define the problem_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#stages-of-analysis)
In this dataset, we have some chemical variables about types of wine, and the goal is to understand how these parameters are related to the quality and how we can improve the quality of the wine. The variables are:

* Alcohol
* Volatile Acidity
* Fixed Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Density
* Total Sulfur Dioxide
* pH
* Sulphates
* Free Sulfur Dioxide

### _2. Collect Data_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#stages-of-analysis)
The data was extracted from the file `wine_quality.xlsx`, from `Kaggle`, availabre at: <https://www.kaggle.com/datasets/yasserh/wine-quality-dataset>.

### _3. Data Cleaning and Preprocessing_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#stages-of-analysis)
Using the library [pandas](https://pandas.pydata.org/docs/) to import and interprete the data:

    import pandas as pd
    
    wine_df = pd.read_excel('wine_quality.xlsx')
    wine_df.info()
In this case, after analysing the resume of informations (columns name, number of rows and data type) it was noted that there isn't `NaN`values, but the `ID` column was named wrongly and the `Type` column can't helps a lot. So:

    wine_df = wine_df.rename(columns{'Unnamed 0':'ID'})
    wine_df = wine_df.drop(['Type'], axis = 1)

### _Calculating the initial wine quality's mean_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#stages-of-analysis)
With the dataset informations, the initial quality mean is:

    initial_mean = wine_df['quality'].mean()

The initial mean is `5.812`.

### _4. Data Analysis Techniques_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#stages-of-analysis)
A mean of `5.812` it's very low about quality. So, the challenge is reach out `7.000`, at least. To help with this challenge, it will be used two artifices: a `Pearson's correlation matrix` and `histogram graphics`, to understand how the variables can interefe in the quality and how they are related to each other. 

### _5. Exploratory Data Analysis (EDA) and Interpretation of Results_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#stages-of-analysis)
The `Pearson's correlation` is very useful in data analysis, because it can show if there's any correlation (weak or strong, direct or indirect) among variables. The libraries [pandas](https://pandas.pydata.org/docs/) and [seaborn](https://seaborn.pydata.org/#) help us with, using the funtion `.corr()` from `pandas` and the `heatmap` from `seaborn`.

    import seaborn as sns
        
    correlation = wine_df.corr()
    sns.heatmap(correlation, annot = True, fmt = ".1f", vmax = 1, vmin = -1)

![Pearson's Correlation](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/0e6b05cd-11fb-4688-90ea-500295cfaaa9)

Analysing the matrix, the most part of the correlations are very weak. Only two correlations are relatively strong: `density` with `alcohol (-0.7)` and `total sulfur dioxide` with `free sulfur dioxide (+0.7)`. In this case, we can predict that the lower density is, higher the alcohol will be and vice versa (strong negative correlation) and lower the total sulfur dioxide is, higher the free sulfur dioxide will be and vice versa (strong positive correlation). When looking at the quality column, there isn't any variable who has a strong correlation. The highest value is `+0.4` (correlation between `quality` and `alcohol`), a weak correlation.

About graphical analysis, some graphics were generated, relating the quality and chemical parameters, using the library [plotly.express](https://plotly.com/python-api-reference/plotly.express.html).

    import plotly.express as px
        
    for coluna in wine_df.columns:
        grafic = px.histogram(wine_df, x = coluna, color = 'quality')
        grafic.show()
            
Analysing the informations above, some insights could be get:

**_Quality x Alcohol:_** The `bests types` of wine have `more alcohol` in its composition compared with the worsts ones. Analysing deeply the graphic, values `higher` than `10.920` can be interesting.
![quality_x_alcohol-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/e62472c8-9308-4f35-9fdd-03edc2da0d7d)

**_Quality x Volatile Acidity:_** The `bests types` of wine have a volatile acidity `between 0.150 and 0.450` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 0.280 and 0.370` can be interesting.
![quality_x_volatile_acidity-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/4edb4e0e-4b96-4fac-958c-f6dbd9ae33cc)

**_Quality x Fixed Acidity:_** The `bests types` of wine have a fixed acidity `between 6.000 and 7.500` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 6.600 and 7.300` can be interesting.
![quality_x_fixed_acidity-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/dd196626-dd8e-4fc9-ac1c-b192ae05bdf2)

**_Quality x Citric Acid:_** The `bests types` of wine have a citric acid `between 0.250 and 0.400` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 0.280 and 0.320` can be interesting.
![quality_x_citric_acid-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/0806a314-9134-47f6-822f-f3af68c16a05)

**_Quality x Residual Sugar:_** The `bests types` of wine have a residual sugar `between 1.000 and 7.000` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 2.300 and 6.200` can be interesting.
![quality_x_residual_sugar-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/078f6651-8fd5-4b48-9ec9-7afc51c467aa)

**_Quality x Chlorides:_** The `bests types` of wine have `less chlorides` in its composition compared with the worsts ones. Analysing deeply the graphic, values `lower` than `0.034` can be interesting.
![quality_x_chlorides-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/707adb0f-8da3-49e1-aa32-8e0cc6a50574)

**_Quality x Density:_** The `bests types` of wine have density `between 0.980 and 0.990` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 0.989 and 0.992` can be interesting.
![quality_x_density-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/89cbe9c0-8cda-46e2-80fa-ff8ce98dd60d)

**_Quality x Total Sulfur Dioxide:_** The `bests types` of wine have total sulfur dioxide `between 80 and 150` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 80 and 129` can be interesting.
![quality_x_total_sulfur_dioxide-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/835640a9-a1b5-4062-9c50-3516897001a4)

**_Quality x pH:_** The `bests types` of wine have pH `between 2.850 and 3.600 in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 2.890 and 3.540 can be interesting.
![quality_x_pH-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/d15a7c73-3a5a-4b4a-b791-cb0decf55087)

**_Quality x Sulphates:_** The `bests types` of wine have sulphates `between 0.300 and 1.000` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 0.360 and 0.900` can be interesting.
![quality_x_sulphates-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/383faa72-c33f-44d7-b91c-46ef1df82744)

**_Quality x Free Sulfur Dioxide:_** The `bests types` of wine have free sulfur dioxide `between 20 and 70` in its composition compared with the worsts ones. Analysing deeply the graphic, values `between 20 and 64` can be interesting.
![quality_x_free_sulfur_dioxide-min](https://github.com/JPedroPy/Wine_Quality_Data_Analysis/assets/141521444/51190c01-fcba-4c45-bae6-59d1ac670d57)

The graphics above reforce the results of Pearson's correlation matrix: the most part of the density are very low and the alcohol high, as well as sulfur dioxide and free sulfur dioxide are low.

### _Setting chemical parameters and calculating new mean_
Now, taking the `bests values` for each column and filtering them, the tendency is `improve the quality`. Checking this up:

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

        new_mean_quality = wine_df['quality'].mean()

The new mean is `7.104`.

### _6. Conclusion and Recommendations_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Wine_Quality#stages-of-analysis)
Adopting `strategical values` was able to `improve` the wine quality by `22.23%` (from `5.812` to `7.104`). Therefore, the wine-producing company should focus on the `range of values` for each chemical parameter:

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

The `critical` parameter is `density`, as it has the narrowest range of values (`0.989` to `0.992`). Therefore, it requires the highest precision in order to cover the range effectively. Consequently, producing wines with these parameters above will likely result in a delightful wine to enjoy.








    
    


