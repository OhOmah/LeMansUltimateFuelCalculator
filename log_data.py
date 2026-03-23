'''
PURPOSE OF THIS SCRIPT: 

This script logs important driver data in Le Mans Ultimate (LMU) and saves to a .csv for further analysis

TODO: 
1. Remove logging to Pandas Dataframes, log data as json/dict variables and export as such. 
This will lighten the load on users computers and speed up the program. We can do the analysis portion for 
the analysis program 
'''

import pandas as pd 
import numpy as np 

import requests
import time

# Start with the function that logs all the inputs and saves to the respective dataframes
def log_driving():
    # Create the first row for the raw input dataframe
    first_input = requests.get("http://localhost:6397/rest/options/liveInputs").json()
    # Create the first row for the usage dataframe as well as the name of user
    first_usage = requests.get("http://localhost:6397/rest/strategy/usage").json()
    name = requests.get("http://localhost:6397/rest/profile/").json()["name"]

    # Convert to dataframe
    input_logging = pd.DataFrame().from_dict(first_input['liveInputs']['di'][0]['raw inputs'], orient='index').T
    usage_logging = pd.DataFrame().from_dict(first_usage[name])

    # Now log every other instance 
    try:
        while True:
            # Grab the raw dict
            new_input = requests.get("http://localhost:6397/rest/options/liveInputs").json()

            # Append to newly created DataFrame object
            new_row = pd.DataFrame().from_dict(new_input['liveInputs']['di'][0]['raw inputs'], orient='index').T
            input_logging = pd.concat([input_logging, new_row], ignore_index=True)
            time.sleep(.05)
    except KeyboardInterrupt:
        print("Logging Completed")
        pass
    

