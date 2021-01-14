"""Pandas Dataframe helper functions"""

import pandas as pd
import numpy as np

class DfHelper:
    """
    A class that contains various pandas dataframe helper functions
    """
    def __init__(self, df):
        """Iniitialize self"""
        self.df = df

    def null_count(self):
        """Returns the sum of null in each column"""
        return self.df.isna().sum()

    def randomize(self, seed):
        """Returns the df with cells randomized"""
        random_df = self.df
        for _ in range(seed):
            random_df = random_df.sample(frac=1, axis=0).reset_index(drop=True)
            random_df = random_df.sample(frac=1, axis=1).reset_index(drop=True)
        return random_df

if __name__ == "__main__":
    print("File loaded and running successfully")