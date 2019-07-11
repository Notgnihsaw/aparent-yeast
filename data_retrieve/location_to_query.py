#This file formats lines and files into a queryable format.

def to_query_line(location, padding):
	
	#region
	loc_list = location.split('_')
	region = ':{0}..{1}'.format(int(loc_list[1]) - padding, int(loc_list[1]) + padding)
	
	#chromosome
	chromosome = loc_list[0].replace('chr', '')
	#chromosome = loc_list[0]
	
	#strand
	if '-' in loc_list[2]:
		strand = ':-1'
	elif '+' in loc_list[2]:
		strand = ':1'
        
	return chromosome + region + strand

#TODO: go through the file line by line and make it queryable
    
def to_query_file(file, padding):
    SiteCounts = open(file)

    lines = SiteCounts.readlines()
    #read in the file, read its lines. 

    for i in range(len(lines)):
        lines[i] = to_query_line(lines[i], padding)
        #format each line of the file.

    #write to the new file.
    filename = file.replace(".txt", '_query_format.txt')
    write_file = open(filename, "w+")

    for i in range(len(lines)):
        write_file.write(lines[i] + '\n')
    
    write_file.close()
    
    return filename