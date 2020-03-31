from pathlib import pathlib

'''
author: kachiem

Directory structure via pathlib for Python. 
Makes it easier to access files by name/object.
'''

BASE_DIR = Path('../').resolve() 
DATA_DIR = BASE_DIR / "data"
NB_DIR = BASE_DIR / "notebooks"


if __name__ == '__main__':
    print(PROJECT_DIR)
    print(RAW_DIR)