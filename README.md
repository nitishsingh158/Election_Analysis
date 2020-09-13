# Colorado County Election Analysis

### **Project Overview**
This project includes the audit of a recent local congressional election in Denver. The audit analyses the candidates contesting and the votes cast for the following counties:
 - Arapahoe
 - Denver
 - Jefferson
 #### A summary of the audit process is as follows:
 1. Calculate the total number of votes cast across all the counties.
 2. Get a list of candidates that received votes. 
 3. Calculate the number of votes and percent of total votes cast in each county. 
 4. Calculate the number of votes and percentage of the total number of votes received by each candidate. 
 5. Determine the winner of the election based on the total number of votes received (popular vote).

 ### **Resources**
1.  Data Source: election_results.csv
2. Software: Python 2 or 3
3. Any code editor like VS Code
4. `PyPoll_Challenge.py`

### **Election-Audit Results**
The analysis of the election shows that:
 - There were 369,711 votes cast in the election with distribution as follows:
   - Jefferson: 38,855 votes which are 10.5% of total votes.
   - Denver: 306,055 votes which are 82.8% of total votes.
   - Arapahoe: 24,801 votes which are 6.7% of total votes.
 -The most number of votes were cast in the county of ***Denver***
 - The candidates were:
   - Charles Casper Stockham
   - Diana DeGette
   - Raymon Anthony Doane
 - The candidate results were:
   - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
   - Diana DeGette received 73.8% of the votes and 272,892 number of votes.
   - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
 - The winner of the election was: ***Diana DeGette*** with 73.8% of total votes cast and 272,892 votes. 

![Results](/Resources/Results.png)

### **Election-Audit Summary**
This python script is quite versatile and can be used to analyze other elections as well with a few small modifications. Some examples are:
1. Analyze elections at Township and Municipal level to get detailed information on which specific areas within the counties are more electorally active. This can be achieved by modifying the candidate and county search loop and changing the list assignment based on the additional Township or Municipality column. 
2. Analyze the voting demographics based on individual voter information such as age, gender, race, etc. Similar to the modification suggestion above, this would also need a different list assignment based on which column number corresponds to the demographic information. 
3. This script can also be used for analyzing larger elections which span more a single county such as state elections. This would not need any modification to the code. But if the user wants State level details we will need to line a new dictionary for states and the number of votes per state. 




