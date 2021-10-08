# <u>Iron Realty</u>
Samanthat Nasti, Patrick Ryan, Paul Shin
![HomepriceInc](https://mrwilliamsburg.com/wp-content/uploads/2021/03/williamsburg-home-prices.jpg)

# Overview

Iron Realty is a full-service real estate agency that specializes in providing homeowners with the tools necessary to sell their homes at their maximum potential. We performed an in-depth analysis of public data containing details about home sales in King County, WA. We used this analysis to develop a linear regression model that will help our clients meet their desired sale price goal. We have identified three influential selling price indicators that can be applied to our linear regression model to generate a feasible estimate for our client's home.

# Business Problem
We want our sellers to get the highest sale price possible for their house.
Sellers tell us their target sale price, and we determine if its realistic, or what they need to do to get to that price. Or, even better - if they can ask for more!

# Data
We were provided data on the King County housing market. With this data we were able to extrapolate a few key variables. We created new columns from existing ones in order to take a closer look at what the data was really telling us.

# Results
## Final Regression Model
 ![Screen%20Shot%202021-10-08%20at%209.01.10%20AM.png](attachment:Screen%20Shot%202021-10-08%20at%209.01.10%20AM.png)

![Screen%20Shot%202021-10-08%20at%208.57.58%20AM.png](attachment:Screen%20Shot%202021-10-08%20at%208.57.58%20AM.png)
 - This plot indicates that our model has no overfitting.

**Pros:**
- Our final model has an r-squared-adjusted value of 0.531 and utilizes 6 features which means that we may explain 53.1% of the variance in home prices in the King County area using just those 6 features.
- Our model performs almost equally well with both test and train datasets which means we certainly did not overfit our model.

**Cons:**
- Our RMSE is around 220k USD which lowers our confidence considering the fact that our median home price of our original dataset 450k USD.
- We eliminated a lot of variables so our model is limited to just 6 variables. If we conduct the future analysis, adding more features might result in more accurate model.

 # Variable Visualization
- Bedrooms/SQFT Living Space
- Condition
- Location

## Bedroom/SQFT Living Space
This variable is significant because it concludes that bedrooms are a contributing factor to the price of a home. In order to get a positive return on a renovation or expansion of livable square footage a good suggestion would be to use the space for a bedroom. 
 ![Screen%20Shot%202021-10-08%20at%209.04.24%20AM.png](attachment:Screen%20Shot%202021-10-08%20at%209.04.24%20AM.png)

## Condition of the housing.
The condition of the house is another important statistic. The condition directly contributes to the price of the house when selling it or buying it. As seen below in the box chart as the condition gets better the value of the house goes up.
 ![Screen%20Shot%202021-10-08%20at%209.05.21%20AM.png](attachment:Screen%20Shot%202021-10-08%20at%209.05.21%20AM.png)

## Location of Housing
- We identified a strong correlation between the latitude and home price, so we used latitude in our model to represent the location of the home being evaluated.
- We used our data to generate a map that shows the sale prices of each data point and exactly where it is located.
- In this map, you can see that higher prices for past home sales occur slightly higher up on the map surrounding certain metropolitan areas. Therefore, this information gives us a great starting point in terms of knowing what we can expect to sell the home for based on the surrounding area’s sales in the past.
![lat_visualization.png](attachment:lat_visualization.png)

# Conclusion
- Our modeling process confirmed that there are significant elements that influence the perceived value of a home.
- Based on our King County housing data, we have identified three influential selling price indicators:
 - Location
 - Amount of Bedrooms
 - House Condition

With knowledge of our client’s target sale price, we will assess the feasibility of them successfully selling for their target as the home currently stands. And, we will identify areas for improvement if their home value falls short of their target. Whether it be performing an interior renovation, or perhaps converting an office to a bedroom, we will determine how our client can achieve their goals.

## Navigation of Repository

```
├── Data                                <- Contains the raw datasets
├── Phase2DataVisualization             <- Folder containing charts and graphs generated from code 
├── Phase2Project                       <- Contains used notebooks and visuals
├── .gitignore                          <- Refrence to types of files for Github to ignore
├── Final_Notebook.ipynb                <- Analysis broken down with Jupyter Notebook
├── Presentation.pdf                    <- PDF version of project presentation for Microsoft
└── README.md                           <- Outline and Repo overview

```
