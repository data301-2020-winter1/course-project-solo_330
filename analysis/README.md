# analysis

This directory holds all jupyter notebooks used in the project.

## milestone1.ipynb

Contains the three raw data sets loaded into dataframes in Python.

## milestone2.ipynb

### Loading and Processing

Loads and processes the raw data set from 'lolchallengertotal.csv' into a dataframe called 'loldata' in Python.

The data is loaded using the load_and_process function from 'scripts/python_functions.py' in order to:
   - Combine mutually exclusive (binary) columns into a single more informative column.
       - For example, the binary columns 'blueWin' and 'redWin' can be condensed into a single more informative categorical column.
       - As only a single team can win, it makes more sense to have a column called 'winner' with the value being 'blue' or 'red'. 
   - Drop the original binary columns which are no longer needed. 
   - Rename columns to be more consistent and clear, and to fix spelling and capitalization mistakes. 
   - Order columns in a more appropriate, intuitive, and useful way.
   - Change the time from seconds to MM:SS and create a column for game length.
       - This is important as game length can vastly impact the outcome of the game and what variables are more important. 
       - For example, for long games (>40 mins) the gold difference becomes obsolete (as both team have enough gold for full items, even if one team has a large gold advantage). 
   - Remove 'remakes' (games where a player failed to connnect, so the game is stopped with no winner or loser after 3 minutes). 

### Exploratory Data Analysis

Found the total number of Korean Challenger games in the season split. 
    - 26,737 games
    
Found the total number of wins per side depending on the game length.
    - This was to test whether any side wins significantly more games for a certain game length.
        - It seems game length does not significantly affect which side wins. 
    - These results were also graphed for visual interpretation.
        - The graph made clear that there is a significant difference between the number of short, medium, and long games.

Calculated the average game length.
    - 24 Minutes and 16 Seconds (medium)

Plotted the distribution of game lengths. 
    - The plot follows a normal distribution, with one exception. 
    - At 15 minutes there is a huge spike in games; this is due to 15 minutes being when surrender votes are unlocked. 
        - When a team believes it cannot win the game, they will surrender at 15 minutes rather than play the game out. 
