import os, os.path
import csv
import pandas as pd
import math
import numpy as np
from random import *

#store file path
fpath = '/Volumes/GoogleDrive/My Drive/BAN_675_Project/Raw Data/'
#collect names of all CSV files in dir
files = [f for f in os.listdir(fpath) if (os.path.isfile(fpath+f) and f[-3:] == 'csv')]
#print(files)

#determine the number of files, then determine how many random rows per file to take
#   in order to get closest to the numer of rows desired
desired_rows = 1000
num_files = len(files)
num_rows_per = math.ceil(desired_rows/num_files)
num_rows_tot = num_files*num_rows_per
#print(num_files,num_rows_per,num_rows_tot)
findex=0
row_sample = list()

for f in files:
    rindex=0
    findex = findex+1
    print("File "+str(findex))
    
    row_indices = []
    df = pd.read_csv(fpath+f, header=0)
    #print(df)
    
    
    rows = len(df.index)
    for i in range(1,num_rows_per+1):
        overflow_counter = 0
        #rindex=rindex+1
        #print("Row "+str(rindex))
        
        # 'do-while' type loop to prevent duplicated rows
        while True:
            row = np.random.randint(1,rows)
            overflow_counter+=1
            if row not in row_indices:
                break
            if overflow_counter > 1000:
                break
        row_indices.append(row)
        row_sample.append(df.loc[row].at["abstract"])
    #if findex ==10:
        #break

df = pd.DataFrame(columns=["abstract"], data=row_sample)
#print(df)
df.to_csv('random_sample.csv')


    


