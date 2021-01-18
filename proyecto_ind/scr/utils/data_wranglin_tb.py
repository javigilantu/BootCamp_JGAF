import numpy as np 
import pandas as pd
import sys, os

driver_standigs = pd.read_csv("C:\\Users\\javig\\OneDrive\\Documents\\Bootcamp\\proyect1_data\\drivers_championship_1950-2020.csv")


world_champions = driver_standigs[driver_standigs["Position"]=="1"]
world_champions

def importer():
    world_champions = driver_standigs[driver_standigs["Position"]=="1"]
    return world_champions

def importer_rw():
    
    winners = pd.read_csv("C:\\Users\\javig\\OneDrive\\Documents\\Bootcamp\\proyect1_data\\race_wins_1950-2020.csv")
    return winners



def add_to_my_path_dir ():
    """
    TODO
                        ---What it does---
    This function adds the libraries current path to your pc path directory.

                        ---What it needs---
    - 

                        ---What it returns---
    This function does not return anything
    """
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))
    print(CURR_DIR)
    CURR_DIR = sys.path.insert(0, 'Dibmar_rep\DAANMO_Project\src_libs\data_hunter.py')
    sys.path.append(CURR_DIR)
    for path in sys.path:
        print(path)
#add_to_my_path_dir()