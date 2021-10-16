import csv
import time
import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=f'logs/ListGenerator {datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")}.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

class tempPlayer():

    def is_valid(self):
        return self.username != "" and self.angelusername != "" and self.mortalusername != ""

    def separate_args_with_commas(self, *args):
        args = map(lambda x: str(x), args)
        return ",".join(args)

    def to_csv_row(self):
        return self.separate_args_with_commas(self.username, self.angelusername, self.mortalusername)

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.angelusername = kwargs.get('angelusername')
        self.mortalusername = kwargs.get('mortalusername')


# GLOBALS: change to name of final players csv you want to use
# NOTE: To make this FINALPLAYERSFILE from the excel generated by the other python code,
#   1: Open the Excel file. In the cells of the 2nd column, transpose the first column onto every row.
#   2: Delete the first column
#   3: Then, delete the columns / ignore the values from Column 4 onwards
#   4: Delete the last row, and then in the new last row, fill in the last empty blank (should be on the 3rd column)
#   5: The generated csv template can be used in Elgene's Angels Mortals Bot
FINALPLAYERSFILE = "test.csv"

def read_csv(filename):
    person_list = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
                playerAngel=row[0].strip().lower()
                playerUsername=row[1].strip().lower()
                playerMortal=row[2].strip().lower()

                new_person = tempPlayer(username = playerUsername,
                    mortalusername = playerMortal,
                    angelusername = playerAngel)
                person_list.append(new_person)
                logger.info(f'Adding ' + str(new_person))
                print(f'Adding ' + str(new_person))
                line_count += 1
        print (f'Processed {line_count} lines.')
        logger.info(f'Processed {line_count} lines.')
        logger.info(f'person_list has been processed successfully')
    return person_list

def write_to_csv(player_list):
    '''
    Writes a variable number of player lists to csv
    '''
    if player_list is not None:
        print (f"Length of list: {len(player_list)}")
        cur_time = time.strftime("%Y-%m-%d %H-%M-%S")
        with open(f"Final Player List - {cur_time}.csv", 'w') as f:
            f.write(f"Player, Mortal, Angel")
            f.write("\n")
            for player in player_list:
                f.write(player.to_csv_row())
                f.write("\n")
            f.close()

if __name__ == "__main__":
    print (f"\n\n")
    print (f"=============================================")
    print (f"Elgene's Angel-Mortal csv generator initializing..............")
    print (f"=============================================")
    print (f"\n\n")

    # Get list of Player objects from csv file
    player_list = read_csv(FINALPLAYERSFILE)
    write_to_csv(player_list)

