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

### Research Questions: 

##### Research Question 1: Which objectives are the most important/highest priority?

##### Research Question 2: What early-game events lead to wins in high elo? 

### Exploratory Data Analysis

Found the total number of Korean Challenger games in the season split:
    * 26,737 games
    
Found the total number of wins per side depending on the game length:
    - This was to test whether any side wins significantly more games for a certain game length.
        - It seems game length does not significantly affect which side wins. 
    - These results were also graphed for visual interpretation.
        - The graph made clear that there is a significant difference between the number of short, medium, and long games.

Calculated the average game length:
    - 24 Minutes and 16 Seconds (lower end of medium)
    - This makes sense as a lot of games are forfeited at 15 minutes (see below point) and the estimated average time for a game of League of Legends is 30 minutes. 

Plotted the distribution of game lengths:
    - The plot follows a normal distribution, with one exception. 
    - At 15 minutes there is a huge spike in games; this is due to 15 minutes being when surrender (forfeit) votes are unlocked. 
        - When a team believes it cannot win the game, they will surrender at 15 minutes rather than play the game out. 
        - This saves time when trying to climb ranks and helps players from tilting. 
        - It makes more sense to forfeit a likely lost game and spend those extra 10-15 minutes on a new game. 
        - This result is consistent with the qualitative observations from Korean Challenger League of Legends. 
        - Players on the Korean server are known to forfeit more games in comparison to regions like North America or Europe.

Calculated the percent of games won after taking the first of a specific objective: 
    - The following objectives (first blood, first tower, first dragon, first baron, first inhibitor) are crucial in determining who wins the game, as they are often linked with rewards that give the team that takes the objective an advantage. 
        - For example, first blood and first tower grant an extra amount of gold, which when converted to items gives your team a power advantage, which can then be used to gain more kills and objectives. 
    - In this analysis only first objectives were looked at, as objectives such as second dragons are much easier to obtain once you have secured the objective the first time around (term: snowballing). 
    - It is often difficult to determine which objectives one should focus. 
        - Teams often trade objectives one opposite sides of the map. 
        - The data analysis can help us determine which objective gives us the higher chance of winning. 
    - From our visual representation we can see that from highest to lowest chance of winnings the objectives are:
        - first Inhibitor
        - first Baron
        - first Tower
        - first Dragon
        - first Blood
    - first inhibitor and first baron having the highest win percentage makes sense
        - They are lategame objectives, usually take after multiple kills, dragons, and towers.
        - By the time either team takes a baron or an inhibitor one team is usually clearly ahead. 
            - This a causation vs correlation problem. 
            - Taking baron or an inhibitor helps a team win, but the team was able to take that objective in the first place because they were already winning. 
        - However, we can still gain an insight into how we play the game. 
            - Inhibitors and barons are usually taken around the same time in the game. 
            - If we are in a situation where we are even with the enemy team, then it may be smarter to trade objectives. 
            - Taking inhibitor and letting the enemy team take dragon may be worthwhile. 
            - However, this result must be taken extremely cautiously. 
            - A team may only have been able to take the first inhibitor because they had baron or vice-versa. 
            - A deeper data analyis taking this into account must be done to clearly determine which is a higher priority. 
    - first Tower, Dragon, and Blood are more interesting as they are early game objectives (first 10 minutes). 
        - For a long time I had believed that first dragon should be much higher priority than first tower. 
            - Top laners can often choose to teleport to dragon to help the team secure the objective or they can choose to stay in lane and push for first tower while the enemy team takes dragon. 
            - As a top laner myself this data analysis is highly useful and eye-opening. 
            - It seems first tower leads to significantly more games won than first dragon. 
            - Some intuitive reasoning is:
                - When taking first dragon the whole team receives a buff, however, that buff is very small. 
                - First dragon gives an advantage, but not big enough to where the advantage cannot be made up through farming minions or getting a kill. 
                - First tower gives an advantage to only one or two players, but the advantage is much greater. 
                - The player who gets first tower could receive anywhere between 450 - 800 gold depending on how fast they take the tower. 
                - This is a large enough advantage where the receiver of the first turret gold can snowball their lane. 
                - This advantage is often enough to decide a game it seems.
                - Overall, the gold worth of dragon and first tower are very similar. 
                    - But in the latter case the 'gold' is spread amongst less players, given those players a bigger advantage.
        - First blood is not very interesting as a variable as it is dependant on outplay potential and often hard to trade objectives on.
            - The standard approach already is to push out lane and take towers when the enemy are collapsing to secure a first blood. 
            - This follows what we have discovered in our data analysis.

Calculated the correlation between all variables:
    - The variables with the highest correlation with winning are: 
        - blueWin
            - blueFirstTower             0.45
            - blueFirstInhibitor         0.64
            - blueDragonKills            0.47
            - blueTowerKills             0.71
            - blueInhibitorKills         0.55
            - blueKills (redDeaths)      0.45
            - blueObjectDamageDealt      0.53
            - redFirstTower             -0.45
            - redFirstInhibitor         -0.62
            - redDragonKills            -0.47
            - redTowerKills             -0.71
            - redInhibitorKills         -0.55
            - redObjectDamageDealt      -0.55
    - These all make sense and follow our above analysis for firstTower and firstInhibitor. 
    - The same points about causation and correlation as well as snowballing can be applied to:
        - dragon kills
        - tower kills
        - inhibitor kills
        - objective damage
    - More analysis would have to be done taking into account the complex mechanisms between variables (most are not independent). 
        - For example, having two dragons will make it easier to pick up the third dragon and win the game. 

#### Summary: 
        
Initially my objective was "to figure out which objectives are the most important and what early-game events lead to winning in high-elo". Below are the conclusions to both of my research questions as per the data analysis done in milestone 2. 

##### Research Question 1: Which objectives are the most important/highest priority?
    
A lot more analysis is needed to fully understand every aspect of the game and what objectives should be prioritized. The fundamental problem is that variables are not independent and that causation vs. correlation is unclear.

A possible research question that could be asked is "What objectives lead to a larger snowballing effect?" For example, we could investigate how often a team that takes first dragon captures the elder dragon (a much more powerful dragon that spawns once either team has slain four dragons). 

##### Research Question 2: What early-game events lead to wins in high elo? 

Early game objectives were made a lot clearer. First tower should be prioritized over first Dragon as more game are won when objectives are traded this way. Reasoning for this could be that the advantage gained is spread less thinly over teammates when choosing to take dragon. Teleporting to dragon also leads to a teleport advantage (when your team still has teleport, but the enemy team does not). This means that a subsequent teleport cannot be matched/followed, which could lead to a secondary indirect advantage from choosing to take turret rather than dragon. 

This analysis was highly interesting as I had previously believed that dragon was always the higher priority as it gives all teammates an advantage, even if that advantage was smaller. But the data analysis has helped convince me that the converse it true. If I am every in a 50/50 situation as a toplaner and can choose between teleporting to dragon or pushing for first turret, I will now likely choose to take turret rather than teleport. 







        
        
