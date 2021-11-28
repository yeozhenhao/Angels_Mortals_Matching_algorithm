# Angels & Mortals Matching algorithm for NUS Medicine & Nursing

## Accreditation
Special thanks to **Sriram Sami** for his idea of using Hamilton algorithm with the `networkx` python module.
####
Please check out his website if you want to learn how it works in Angels & Mortals: https://sriramsami.com/archangel/

## What I changed
- changes of player's preferences for NUS Medicine & Nursing faculty (e.g. CG number, House number)
####
- an important one-line replacement of a deprecated `networkx` command in **arrange.py** so the algorithm works with the latest `networkx==2.6.3`.
####
- **NEW .csv output functions:**\
1: Output .csv only prints when matching algorithm successfully matches >80% of players in the inital .csv input file.\
2: Also, log file will record a list of Telegram usernames which failed to get a match and are thus not included in the CSV output. They will need to be matched manually.
####
- **Other minor changes:**\
1: Changed all of the `print` command formatting to the new-style `print (f'.......')` commands to fix issues running on Python==3.9\
2: Now reads .csv files with header columns\
3: Added logging for various functions for easier readability & debugging\
4: New requirements.txt file with the latest versions of required python modules (tested working as of October 2021)

## What I added
- **transpose_for_bot.py** script to easily transpose the output .csv data, so they can be easily loaded into my [Angel and Mortals Dual Telegram Bots](https://github.com/yeozhenhao/Angels_Mortals_bot) to start an Angels and Mortals game.\
Running **transpose_for_bot.py** will re-export the output .csv file with the assigned Angels & Mortals for each player, and then the new .csv can be used as input for my other Python app ***[Telegram Dual Bots for Angels & Mortals](https://github.com/yeozhenhao/Angels_Mortals_bot)***.\
*Note: This file is not necessary in the running of the Matching algorithm.*
#### How to use transpose_for_bot.py
1. Rename output .csv from Matching algorithm as **"1.csv"**, and leave it in the root folder.
2. Run **transpose_for_bot.py**, and a new "Final Player List.csv" should be created with the assigned Angels & Mortals for each player.

### Overview
The matching for Angels & Mortals can be done with a Hamiltonian-cycle based approach to finding valid angel-mortal chains based on player's preferences.\
`networkx` was used for the Hamilton algorithm.

#### TLDR: How matching is done
- ensures have their gender preferences satisfied
- ensures matches are NOT from the same Clinical Group (CG)
- ensures matches are NOT from the same House\
*Note: The % leniency in matching for the above criteria can be set in **arrange.py***
- only if >80% of the entire player base has a suitable match, then a Final Players List .csv output will be generated

### How to use the Matching Algorithm
1. Clone the repo
2. Create a virtual environment so that the required libraries don't pollute your namespace (Optional). Run `virtualenv venv` in the cloned directory.
3. Install requirements with `pip install -r requirements.txt`
4. Put a csv file with headers (see below for the header names; the first row will not be processed) with all details of participants in correct order in a file called `playerlist.csv` in the main folder.
5. Run `python angel.py`
6. Output will be a .csv file with naming format based on time & date at runtime


### Columns required for playerlist.csv
First, playerlist.csv should have a header row with all the column names.

The columns in playerlist.csv should be arranged as such, with 1 being the leftmost column. Important columns for matching: Gender preference, Gender, House number, CG number.


1. Telegram Username
2. Name
3. Gender Preference (for Angel & Mortal)
4. Gender
5. Interests 
6. Two truths one lie
7. Self-introduction (for Mortal only)
8. House Number (in Medicine & Nursing faculty)
9. CG Number (in Medicine & Nursing faculty)
10. Year of Study
11. Faculty

**Output CSV** will have the same columns but no header.\
Players will be arranged such that for each player row in the output .csv file, his/her Angel is in the row above and his/her Mortal is in the row below.

### If you're looking for an Angels & Mortals Telegram Bot
You may check out my other Python repository here:\
https://github.com/yeozhenhao/Angels_Mortals_bot

## Bot functions (in photos)
*I believe that a picture paints a thousand words - yeozhenhao*
####
![Starting the bot & starting your message with @clinicals](botPics/startbot.png)\
***Starting the bot & starting your message with @clinicals***\