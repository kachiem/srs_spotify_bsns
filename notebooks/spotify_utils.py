import numpy as np
import pandas as pd
import glob, os
from pathlib import *
import json

'''  
author: kachiem

Utility functions for spotify 2019 data analysis.
'''


def json_to_array(path):
    ''' 
    Function to convert .json file into numpy array.

    input: String of file path
    output: np.array() object
    '''
    if path != "":
        json = pd.read_json(path)
        np_array = np.asarray(json)
        print(np_array.shape)  
        return np_array
    
    else:
        print("Error: input must be path")