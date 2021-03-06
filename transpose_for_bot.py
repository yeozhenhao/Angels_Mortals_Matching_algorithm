import csv
import time
import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=f'logs/{datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")}.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# GLOBALS: change to name of final players csv you want to use
# NOTE: To make this FINALPLAYERSFILE from the excel generated by the other python code,
#   1: Open the Excel file. In the cells of the 2nd column, transpose the first column onto every row.
#   2: Delete the first column
#   3: Then, delete the columns / ignore the values from Column 4 onwards
#   4: Delete the last row, and then in the new last row, fill in the last empty blank (should be on the 3rd column)
#   5: The generated csv template can be used in yeozhenhao's Angels Mortals Bot
FINALPLAYERSFILE = "1.csv"

import pandas as pd
def read_csv(filename):
    df = pd.read_csv(filename)
    print(df)
    df_new = df.rename(columns={'Telegram Username':'Player', 'Name': 'Angel', 'GenderPref': 'Mortal'})
    print(df_new)
    for i, row in df_new.iterrows():
        # print(i)
        df_new.loc[i, 'Mortal'] = df_new.loc[i, 'Player']  ### DO NOT USE .at || .at will convert the column data into a float/int, which is invalid with a string Telegram username. Use .loc instead!
        df_new.loc[i, 'Angel'] = df_new.loc[i, 'Player']
    print (df_new)
    df_new.loc[:, 'Mortal'] = df_new.Mortal.shift(-1)
    df_new.loc[:, 'Angel'] = df_new.Angel.shift(1)
    print(df_new)
    df_new['Angel'].iloc[[0]]=df_new['Player'].iloc[[-1]]
    print(df_new)
    df_new['Mortal'].iloc[[-1]]=df_new['Player'].iloc[[0]]
    print(df_new)
    # df_new2 = df_new.iloc[:-1,:] ## removing the last row ###THESE FUNCTIONS ARE NOT IMPORTANT - they were made based on an incorrect playerlist template
    # print(df_new2)
    # return df_new2
    return df_new

def write_to_csv(player_df):
    if player_df is not None:
        print (f"Length of list: {len(player_df)}")
        cur_time = time.strftime("%Y-%m-%d %H-%M-%S")
        with open(f"Final Player List - {cur_time}.csv", 'w') as f:
            player_df.to_csv(f, encoding='utf-8', header= True, index = False, line_terminator='\n')
            f.close()
    else:
        print (f"ERROR: player_df is None")

if __name__ == "__main__":
    print (f"\n\n")
    print (f"=============================================")
    print (f"yeozhenhao's Angel-Mortal csv generator initializing..............")
    print (f"=============================================")
    print (f"\n\n")

    # Get list of Player objects from csv file
    player_df = read_csv(FINALPLAYERSFILE)
    write_to_csv(player_df)

