from Algorithms.Data_Analysis.bfcf import all_combos
from tqdm import tqdm


def k_data()):
    '''
       Multithreading to calculate ~20 random samples and ~20 solutions of The
       battery cycler??
       TO DO:
       - multithreading??
       - change data structure in order to be faster!!!
    '''
    for combo in all_combos():
        print(list(combo[1:]))
