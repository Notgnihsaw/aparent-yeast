#This file formats a tab separated siteCount file into a pandas Dataframe.
import pandas as pd

def to_dataframe(filepath):
    tsv = open(filepath, 'r')
    
    loaded = list(zip(*(line.strip().split('\t') for line in tsv)))

    count_dict = {'Location':loaded[0], 'tag_count':loaded[1], 'distinct_tags':loaded[2], 'degeneracy':loaded[3]}

    tsv.close()
    
    return pd.DataFrame(count_dict)