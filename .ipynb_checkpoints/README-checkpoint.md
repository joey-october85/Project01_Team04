# Project01_Team04
Module 7 + 8 Project 01

# Up, Up, Down, Down: 
# An Analysis of Video Games Through the Years
Team 4 | Isaac . Joe . Bahjo . Joey

In this analysis we look a dataset of video game sales from 1980 to 2020 where and dive into the sales trends across the world. We look at data of a wide range of games and platforms from the Atari 2600 to the Xbox One and Playstation 4; From Asteroids to Super Mario Bros. and beyond…

Video Game Sales | https://www.kaggle.com/datasets/gregorut/videogamesales

#### Tasks:
Outline – Joey <br>
Clean Up Process – Team Effort <br>
Summary – Isaac <br>
Visualizations – Team Effort <br>
Powerpoint – Bahjo <br>
Conclusions/Limitations - Joe <br>

Google Slides - https://docs.google.com/presentation/d/1c6DhoCiIgrAcCUEuCiw0veyT5Agcjflmj0PjtigPn6E/edit#slide=id.p


# Questions
Review data from year 2000 and later

#### ISAAC
What were the highest selling games of all time? (BAR GRAPH) <br>
What were the five most active Publishers (2000 - 2016)?
    
#### BAHJO
What were sales breakdown for each regions? (Pie Chart)

#### JOE
What is the genre sales breakdown of all time? (Pie Chart)<br>
How many games released per year? (Line Chart)

#### JOEY
What were the games sales per platform - per year? (Multi Line via Platform)<br>
What were the highest selling games per Platform? (Table) (2000 - 2016)


# Analysis

### Dependencies
- Pandas
- pathlib
- matplotlib
- numpy
- seaborn
- plotly (express)

Dataset CSV file identified with pathlib and converted to dataframe. This initial dataframe will be used as the basis for all subsequent dataframes/analysis.

## Joey's Analysis (Platform)
Cleaned the initial dataframe to remove null valuesfrom Year of Release and Publisher columns, and converted Year column values from float to int.

Little to no usable data was found for years 2017 and later and therefore all data for these years were dropped to establish a new dataframe. For presentation purposes only a sample of the data was used (2000 - 2016) for Platform analysis.

Parsed the dataframe further to only include sales data with game name, year of release and platform. This dataframe will be referred to as the gs_df (or game sales dataframe)

The highest value for Global Sales was identified for each platform and converted into it's own dataframe (aka max value dataframe).

The max value dataframe was then merged with the 
game sales dataframe so the we can display all data (name, platform and year of release) for each of the highest selling games for each platform.

Additional exploration of the data was executed to identify yearly sales for each platform by year. This exact data was not used in final presentation, however the dataframe is used in subsequent code (sorted_df).

Two empty lists created for each year that is being analyzed (2006 - 2016) and for each platform that had sales within that date range.

For loops used to fill the empty lists leveraging sorted_df.

Dictionary created using dictionary comprehension to store global sales totals for each platform, per year. This dictionary was then converted to a dataframe (data_df) and the years set as the index.

The dataframe (data_df) was leveraged to build smaller dataframes that we will use for analyzing sales for sub-categories of platforms: Handheld Consoles, Sixth Generation Consoles, and Seventh Generation Consoles.

For each subcategory a dataframe was created (leveraging data_df) to include only data for each subcategory and then used to build multi-line charts with matplotlib and plotly.express.

The same steps were taken to create multi-line chart for all platforms across the date range, however this data and visualization were not used in the final presentation.

A for loop was used to identify the year with the most game sales and total lifetime game sales for each platform.

#### Additional unused analysis
Using the base dataframe, the following game review information was pulled.
 - Highest and lowest number of critic reviews for a single game
 - Average number of critic reviews for all games
 - Highest and lowest number of user reviews for a single game
 - Average number of user reviews for all games
 
 A dataframe was created to show all the score data for games where all null values were dropped and then sorted by the user count in descending order. 
 The top five games based on number of reviews were printed.
 
 ## Joe's Analysis
 
 ## Isaac's Analysis
 
 ## Bahjo's Analysis
 Game Sales Dataframe used to build analysis.
 
Identified the differnt regions and built a list using these column names.
 
Empty list created that will hold each region's sales
 
A for loop is used to retrieve the totals of each region's sales and appended to the empty list.

Function is defined that will be used to display percentages and absolute value in pie chart.

Labels defined for the pie chart and singled out region with highest sales for chart explode.
Pie chart plotted using data, function and configurations stated above, saved file to output folder and displayed chart.