import pandas as pd
import numpy as np

class DfHelper:
    """
    A class that contains various pandas dataframe helper functions
    """
    def __init__(self, df):
        self.df = df

    def null_count(self):
        return self.df.isna().sum()

    def randomize(self, seed):
        self.df = self.df.apply(np.random(seed=seed).permutation, axis=0)
        return self.df.apply(np.random(seed=seed).permutation, axis=1)

if __name__ == "__main__":
    print("File loaded and running successfully")