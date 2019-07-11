#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:20:19 2019

@author: Peter Benson
"""

import location_to_query 
import seq_fetch
import to_df 

import pandas as pd

def read_and_query(filename, padding, return_type = 'df'):
    count_dataframe = to_df.to_dataframe(filename)
    
    query_file = open(location_to_query.to_query_file(filename, padding), 'r')
    
    seq_list = []
    
    for query in query_file:
        seq_list.append(seq_fetch.run('saccharomyces_cerevisiae', query))
    
    print(seq_list)
    print(str(len(count_dataframe)) + '\n' + str(len(seq_list)))
        
    #count_dataframe = count_dataframe.append(seq_list)
    
    sequence_dataframe = pd.DataFrame(count_dataframe)
    
    if return_type == 'df':
        return count_dataframe
    elif return_type == 'seqs':
        return seq_list
    else:
        print("return_type invalid, please specify either df (dataframe) or seqs (sequences).")
    

yeast_df = read_and_query("SiteCounts/site_count_test.txt", 10, 'df')


yeast_df.to_csv('yeast_df_site_count', sep='    ')

