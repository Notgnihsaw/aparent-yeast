#TODO: make a dict of the .txt file
'''import re
import csv'''
import pandas as pd

def to_dataFrame(filepath):
    tsv = open(filepath, 'r')
    
    return list(zip(*(line.strip().split('\t') for line in tsv)))


loaded = load_tsv("DHch01_20nt_Ttrim_siteCount.txt")

count_dict = {'Location':loaded[0], 'tag_count':loaded[1], 'distinct_tags':loaded[2], 'degeneracy':loaded[3]}

df = pd.DataFrame(count_dict)