import pandas as pd
import numpy as np

def categ(df):
    """
    Recibe un dataframe y le modifica las variables categóricas.
    """
    cutval = {"Fair":1, "Good":2, "Very Good":3, "Premium":4, "Ideal":5}
    clarval = {"FL":12, "IF":11, "VVS1":10, "VVS2":9, "VS1":8, "VS2":7, "SI1":6, "SI2":5, "SI3":4, "I1":3, "I2":2, "I3":1}
    colval = {"D":100, "E":93, "F":85, "G":77, "H":66, "I":53, "J":44}
    df.cut = df.cut.apply(lambda x: cutval[x])
    df.clarity = df.clarity.apply(lambda x: clarval[x])
    df.color = df.color.apply(lambda x: colval[x])

    return df