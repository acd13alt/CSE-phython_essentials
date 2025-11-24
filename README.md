# CSE-phython_essentials
This Python script, tournament_search.py provides a simple, interactive console application for looking up the winners of two major football tournaments: the FIFA World Cup and the UEFA Champions League (UCL) for those enthusiatic fans and lovers of this beautiful game called football.

The system uses pre-defined data sets (Python dictionaries) to quickly retrieve winner information based on the year of the tournament.

Features
Search FIFA World Cup Winners: Look up the winner of a specific World Cup year (data available from 1930 to 2022).

Search UEFA Champions League Winners: Look up the winner of a specific UCL season (data available from 2000 to 2025).

View All Winners: Display a complete list of all the FIFA World Cup and UCL winners included in the current data sets.

Simple Menu Interface: Easy navigation through a number-based menu in the console.

How to Run the Program
Prerequisites
You need to have Python installed on your system. This script is compatible with Python 3.

Running
Save the entire Python code (including the dictionaries and functions) into a file named tournament_search.py.

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script using the following command:

Bash

python tournament_search.py
How to Use the Menu
Once you run the script, the main menu will appear:

  *FOOTBALL WINNERS SEARCH*
1. Search FIFA World Cup Winner
2. Search UEFA Champions League Winner
3. View All FIFA Winners
4. View All UCL Winners
5. Exit

Enter your choice (1-5): 
To find a winner: Enter 1 or 2 and press Enter. The system will prompt you to input the year.

To view a complete list: Enter 3 or 4 to see all the stored winner data.

To exit the program: Enter 5.

Data Sources
The winner data is stored in the following variables:

fifa_world_cup_winners: Contains FIFA World Cup winners from 1930 to 2022.

ucl_winners: Contains UEFA Champions League winners from 2000 to 2025.
