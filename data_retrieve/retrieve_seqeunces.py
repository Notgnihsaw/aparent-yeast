#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:20:19 2019

@author: Peter Benson
"""

import location_to_query 
import seq_fetch

import pandas as pd
import csv

def to_dict(filepath):
    tsv = open(filepath, 'r')
    
    loaded = list(zip(*(line.strip().split('\t') for line in tsv)))

    count_dict = {'Location':loaded[0], 'tag_count':loaded[1], 'distinct_tags':loaded[2], 'degeneracy':loaded[3]}

    tsv.close()
    
    return count_dict


def read_and_query(filename, padding, return_type = 'dict'):
    site_count_dict = to_dict(filename)
    
    query_file = open(location_to_query.to_query_file(filename, padding), 'r')
    
    seq_list = []
    
    for query in query_file:
        seq_list.append(seq_fetch.run('saccharomyces_cerevisiae', query))
    
    #print(seq_list)
    #print(str(len(site_count_dict)) + '\n' + str(len(seq_list)))
    
    site_count_dict['sequence'] = seq_list

    if return_type == 'dict':
        return site_count_dict
    elif return_type == 'df':
        return pd.DataFrame(site_count_dict)
    elif return_type == 'seqs':
        return seq_list
    else:
        print("return_type invalid, please specify either dict (dictionary) or seqs (sequences).")
        
'''def write_to_csv(input_dict, csv_name, columns):
    with open(csv_name, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        for data in input_dict:
            writer.writerow(data)'''
    

yeast_df = read_and_query("SiteCounts/site_count_test.txt", 10, 'df')

yeast_df.to_csv('SiteCounts/site_counts_with_sequence.csv')