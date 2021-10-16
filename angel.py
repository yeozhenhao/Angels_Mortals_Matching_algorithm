'''
tAngel angel-mortal matching code
Author: Sriram Sami + Elgene 2021 update
Version: 0.0.1



Program input: List of participants
Program output: Participants matched to each other forming either a) one complete ring or b) multiple complete rings. No lone particpants are allowed.

Priorities (decreasing order) [must be done]:
1) Forming complete circles (everyone MUST have an angel and mortal)
2) Respecting gender choices

Optimization objective - get people you DON'T KNOW AT ALL
Optimization priorities:
1) Angel - Mortal relationship - they must not know each other as much as possible
- Achieved by separating by HOUSE (floor) and FACULTY

Distance (or whether an edge exists between two nodes) is a function of:
1) Whether they are of different houses
2) Whether their faculties are different
'''
# IMPORTS
import csv
import time
import random
import logging
import datetime
# # FROMS
# from models import Player
# from arrange import angel_mortal_arrange

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=f'logs/{datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")}.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)




# GLOBALS
PLAYERFILE = "playerlist.csv"

# Constants
GENDER_MALE = "Male"
GENDER_FEMALE = "Female"
GENDER_NONBINARY = "Non-binary"
GENDER_NOPREF = "No preference"

GENDER_SWAP_PREFERENCE_PERCENTAGE = 0.0


class Player():
    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.playername = kwargs.get('playername')
        self.housenumber = kwargs.get('housenumber')
        self.cgnumber = kwargs.get('cgnumber')
        self.genderplayer = kwargs.get('genderplayer')
        self.yearofstudy = kwargs.get('yearofstudy')
        self.genderpref = kwargs.get('genderpref')



def read_csv(filename):
    person_list = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                logger.info(f'Column names are {", ".join(row)}')
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:

                playerUsername=row[0].strip().lower()
                playerName=row[1].strip().lower()
                houseNumber=row[2].strip().lower()
                CGnumber=row[3].strip().lower()
                genderPlayer=row[4].strip().lower()
                yearofStudy=row[5].strip().lower()
                genderPref=row[6].strip().lower()

                new_person = Player(username = playerUsername,
                    playername = playerName,
                    housenumber = houseNumber,
                    cgnumber = CGnumber,
                    genderplayer = genderPlayer,
                    yearofstudy = yearofStudy,
                    genderpref = genderPref)
                person_list.append(new_person)
                logger.info(f'Adding ' + str(new_person))
                print(f'Adding ' + str(new_person))
                line_count += 1
        print (f'Processed {line_count} lines.')
        logger.info(f'Processed {line_count} lines.')
        logger.info(f'person_list has been processed successfully')
    return person_list





def separate_players(player_list):
    '''
    Separates the list of player list into male_male, male_female, and
    female_female gender preference lists
    '''
    male_male_list = []
    male_female_list = []
    female_female_list = []

    for player in player_list:
        if (player.genderplayer == 'male' and player.genderpref == 'male') or (player.genderplayer == "non-binary" and player.genderpref == "male"):
            male_male_list.append(player)
            print(f'Added Player: {player.username}, Gender: {player.genderplayer}, GenderPref: {player.genderpref} to male_male_list')
            logger.info(f'Added Player: {player.username}, Gender: {player.genderplayer}, GenderPref: {player.genderpref} to male_male_list')
        elif (player.genderplayer == 'female' and player.genderpref == 'female') or (player.genderplayer == "non-binary" and player.genderpref == "female"):
            female_female_list.append(player)
            print(f'Added Player: {player.username}, Gender: {player.genderplayer}, GenderPref: {player.genderpref} to female_female_list')
            logger.info(f'Added Player: {player.username}, Gender: {player.genderplayer}, GenderPref: {player.genderpref} to female_female_list')
        else:
            male_female_list.append(player)
            print(f'Added Player: {player.username}, Gender: {player.genderplayer}, GenderPref: {player.genderpref} to male_female_list')
            logger.info(f'Added Player: {player.username}, Gender: {player.genderplayer}, GenderPref: {player.genderpref} to male_female_list')
    return (male_male_list, male_female_list, female_female_list)

def savegenderlist(genderlist: list):
    temp = []
    for k, v in players.items():
        temp[k] = v.genderplayer
        temp[k] = v.genderpref

    with open(genderlist.json, 'w+') as f:
        json.dump(temp, f)

playerList = read_csv("playerlist.csv")

gendermatchinglist = separate_players(playerList)
# savegenderlist(male_male_list)