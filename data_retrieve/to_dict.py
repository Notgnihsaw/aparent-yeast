#TODO: make a dict of the .txt file
import re

def load_file(filepath):
    file = open(filepath, 'r')
    
    #chrIII_101162_+	2	1	1
    #chrIII_101242_-	1	1	1

    
    lines = file.readlines()
    
    return lines


def format_row(row, larger_file, index)
    plussearch = re.search('[+-]', row)
    
    digit_start = plussearch.start() + 2
    
    formatted_row = [0]*4
    
    formatted_row[0] = row[0:digit_index-1]
    formatted_row[1] = row[digit_index:re.search('\t', row[digit_index:]).start()]
    formatted_row[2] = row[re.search('\t', row[digit_index:]).start()+1:]
    