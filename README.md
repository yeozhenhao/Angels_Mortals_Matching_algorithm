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

### Overview
The matching for Angels & Mortals can be done with a Hamiltonian-cycle based approach to finding valid angel-mortal chains based on player's preferences.\
`networkx` was used for the Hamilton algorithm.

### How to use
1. Clone the repo
2. Create a virtual environment so that the required libraries don't pollute your namespace (Optional). Run `virtualenv venv` in the cloned directory.
3. Install requirements with `pip install -r requirements.txt`
4. Put a csv file with headers (see below for the header names; the first row will not be processed) with all details of participants in correct order in a file called `playerlist.csv` in the main folder.
5. Run `python angel.py`
6. Output will be a .csv file with naming format based on time & date at runtime


### Columns required for playerlist.csv
First, playerlist.csv should have a header row with all the column names.

The columns in playerlist.csv should be arranged as such, with 1 being the leftmost column. Important columns for matching: Gender, Gender preference, House number, CG number 


1. Telegram Username
2. Name
3. Gender
4. Gender Preference (for Angel & Mortal)
5. House Number (in Medicine & Nursing faculty)
6. CG Number (in Medicine & Nursing faculty)
7. Year of Study
8. Faculty
9. Interests
10. Two truths one lie
11. Self-introduction (for Mortal only)

**Output CSV** will have the same columns but no header.\
Players will be arranged such that for each player row in the output .csv file, his/her Angel is in the row above and his/her Mortal is in the row below. 