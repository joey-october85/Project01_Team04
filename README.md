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
 
### Conlcusion 
What were the games sales per platform - per year? (Multi Line via Platform)<br>

Nintendo DS was the highest video game seller for the Handheld consoles (2000 - 2016)
- Total Game Sales: 
- 891.74

- Year with the highest sales:<br>
  2009 (207.08 sales)
    
- Top Contributing Game:<br>
   New Super Mario Bros. (29.80 sales)

![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/Fig1.png?raw=true "Fig1-1")
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig1-2.png?raw=true "Fig1-2")

Sony’s Playstation 2 was the highest video game seller for the 6th Generation of consoles.
- Total Game Sales: 1,233.5

- Year with the highest sales:<br>
    2004 (211.78 sales)    

- Top Contributing Game:<br>
    Grand Theft Auto: San Andreas (20.81 sales)

![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/Fig2.png?raw=true "Fig2-1")
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig2-2.png?raw=true "Fig2-2")

Nintendo Wii was the highest video game seller for the 7th Generation of consoles (2000 - 2016).

- Total Game Sales: 891.74

- Year with the highest sales: <br>
    2009 (207.08 sales)

- Top Contributing Game:<br>
    Wii Sports (82.53 sales)

![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/Fig3.png?raw=true "Fig3-1")
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig3-2.png?raw=true "Fig3-2")



Sales for all platforms 2000 - 2016
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig4.png?raw=true "Fig4-1")
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig4-2.png?raw=true "Fig4-2")

What were the highest selling games per Platform? (Table) (2000 - 2016)

| Syntax      | Highest Selling Games per Platform | | | |
| :---        |    :----:   |          ---: |          ---: |          ---: |
| Rank      | Title       | Platform| Release Date| Global Sales (in millions)|
| 1   | Wii Sports        | Wii| 2006|82.53|
| 2   | New Super Mario Bros.        | DS| 2006|29.8|
| 3   | Kinect Adventures!        | X360| 2010|21.81|
| 4   | Grand Theft Auto V        | PS3| 2013|21.04|
| 5   | Grand Theft Auto: San Andreas        | PS2| 2004|20.81|
| 6   | Pokèmon Ruby/Pokemon Sapphire        | GBA| 2002|15.85|
| 7   | Call of Duty: Black Ops 3        | PS4| 2015|14.63|
| 8   | Pokèmon X/Pokemon Y        | 3DS| 2013|14.6|
| 9   | Halo 2        | XB| 2004|8.49|
| 10   | The Sims 3        | PC| 2009|8.01|
| 11  | Grand Theft Auto: Liberty City Stories        | PSP| 2005|7.69|
| 12  | Call of Duty: Black Ops 3        | XOne| 2015|7.39|
| 13  | Mario Kart 8        | WIIU| 2014|7.09|
| 14  | Super Smash Bros. Melee        | GC| 2001|7.07|
| 15  | Pokèmon Crystal Version        | GB| 2000|6.39|
| 16  | Final Fantasy IX        | PS| 2000|5.3|
| 17  | The Legend of Zelda: Majora's Mask        | N64| 2000|3.36|
| 18  | Minecraft        | PSV| 2014|1.96|
| 19  | Crazy Taxi        | DC| 2000|1.81|
| 20  | Final Fantasy        | WS| 2000|0.51|


 
 ## Joe's Analysis
 For the project 1 code the code imports and reads the csv file for the video game data so it can be analyzed. First the code creates a data frame for the csv file to make it easier to read. Then using .loc the data frame drops any data after the year 2017 since there was not sufficient information on the csv file after that year. Using the clean data the total number of games released was needed. The code calculates the total number of games using .value_counts and then sort_index to put them in order by year. Using this code a line graph is made to show a better visual representation of the release of games each year. Next the total number of games released by genre is needed to be found. Using value_counts again and counting all the Genre tags for the video games a list is made of the total genre of games. Finally using this list a pie chart is created to make a visual representation of how many of each genre of games were released from 1980-2016.
 

How many games released per year?
- Games released (1980-2016)
- 2008 had the highest amount of games released at 1,427
- 2006-2011 had over 7,000 games released
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig5.png?raw=true "Fig5")

What is the genre sales breakdown of all time? (Pie Chart)
- Games released by genre from 1980-2016
- Action was the most popular genre of games released making up 20.1% of all games released
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig6.png?raw=true "Fig6")

 ## Isaac's Analysis
 In this project I found the highest and lowest selling game of all time. We decided to just present the highest selling game because the global sales weren’t accurate for the lower selling games. The data was in millions so the lowest selling games were labeled at 0.01 million.
 
We cleaned up the data frame to only show the sales, because that’s what we were focusing on. 

I created a bar graph to show the top 50 highest selling games of all time. The lables of the chart weren’t clean and the names were to long. So I created a code that changed the labels on the x axis to the “Pub” aka publishers.
Instead of doing the lowest selling games I decided to do the “Top 5 selling publishers”. 

I created a code that pulled the top 5 publishers and their value counts for number of releases. I then created a bar graph for them. To put the icing on the cake, I then got each of these publishers highest selling game from the csv file. 

What were the highest selling games of all time? (BAR GRAPH)
Wii Sports
- Platform: Nintendo Wii
- Release Year: 2006
- Units Sold: 82.53 Million
![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig9.png?raw=true "Fig9")

![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/Fig8.png?raw=true "Fig8")

What were the five most active Publishers (2000 - 2016)?

- Electronic Arts: 1356. <br>
    FIFA 2016


- Activision: 985 <br>
    Call of Duty: Modern Warfare 3


- Namco Bandai Games: 939<br>
    Namco Museum


- Ubisoft: 933 <br>
    Just Dance 3


- Konami Digital Entertainment: 834<br>
    Metal Gear Solid 2: Sons of Liberty

![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/fig10.png?raw=true "Fig10")


 ## Bahjo's Analysis
 Game Sales Dataframe used to build analysis.
 
Identified the differnt regions and built a list using these column names.
 
Empty list created that will hold each region's sales
 
A for loop is used to retrieve the totals of each region's sales and appended to the empty list.

Function is defined that will be used to display percentages and absolute value in pie chart.

Labels defined for the pie chart and singled out region with highest sales for chart explode.
Pie chart plotted using data, function and configurations stated above, saved file to output folder and displayed chart.

What were sales breakdown for each regions? (Pie Chart)

Breakdown of total sales for each market.
- U.S. had the most sales of all regions.
- 3,523MM units sold

![Alt text](https://github.com/joey-october85/Project01_Team04/blob/main/Output/Fig7.png?raw=true "Fig7")









