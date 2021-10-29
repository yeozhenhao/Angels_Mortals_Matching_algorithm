# Angels & Mortals Matching algorithm

## Algorithm Author: Sriram Sami
Check out his website for more details! https://sriramsami.com/archangel/

## 2nd Author: Elgene Yeo
I do not take credit for the original algorithm using the networkx module. I have only made my own changes of player's preferences for NUS Medicine & Nursing faculty, added some of my own columns & an important one-line change in arrange.py so the algorithm works with networkx==2.6.3.


### Overview
Angels & Mortals algorithm uses a Hamiltonian-cycle based approach to finding valid angel-mortal chains based on player's preferences. Critically, `networkx` was used for graph algorithms.

### Usage
1. Clone the repo
2. Create a virtual environment so that the required libraries don't pollute your namespace (Optional). Run `virtualenv venv` in the cloned directory.
3. Install requirements with `pip install -r requirements.txt`
4. Put a header-less tsv file (no column names, the first row is the first row of data already) with all details of participants in correct order in a file called `playerlist.tsv` in the main folder.
5. Run `python angel.py`


### Columns required for playerlist.csv
The columns in playerlist.csv should be arranged as such, with 1 being the leftmost column. Important columns for matching: Gender & Gender preference, House number, CG number 


1. Telegram Username
2. Name
3. House Number
4. CG Number
5. Gender
6. Year of Study
7. Gender Preference (for Angel & Mortal)
8. Faculty
9. Interests
10. Two truths one lie
11. Message for your mortal
