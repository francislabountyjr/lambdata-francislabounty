import pandas as pd
import numpy as np

def null_count(df):
    return df.isna().sum()

def randomize(df, seed):
    df = df.apply(np.random(seed=seed).permutation, axis=0)
    return df.apply(np.random(seed=seed).permutation, axis=1)