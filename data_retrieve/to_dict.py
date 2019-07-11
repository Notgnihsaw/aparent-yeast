#TODO: make a dict of the .txt file
'''import re
import csv'''
import pandas as pd

def to_dataFrame(filepath):
    tsv = open(filepath, 'r')
    
    loaded = list(zip(*(line.strip().split('\t') for line in tsv)))

    count_dict = {'Location':loaded[0], 'tag_count':loaded[1], 'distinct_tags':loaded[2], 'degeneracy':loaded[3]}

    return pd.DataFrame(count_dict)