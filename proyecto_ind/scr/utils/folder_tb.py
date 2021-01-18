import numpy as np
import pandas as pd


def column_erraser(data, col1=None, col2=None,col3=None,col4=None,col5=None):
    
    x = data.drop(data.columns.difference([col1,col2,col3,col4,col5]), 1)
    
    return x

def dataframe_merge (data1, data2, Name):
    
    x = pd.merge(data1, data2, "left", on= [Name])

    return x

def pt_2_df (data, Name ):
     
     x = data.pivot_table(index=[Name], aggfunc= "size")
     y = pd.DataFrame(x)

     return y
