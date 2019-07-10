


def to_query(location):
	
	#region
	loc_list = location.split('_')
	region = ':{0}..{1}'.format(int(loc_list[1]) - 50, int(loc_list[1]) + 50)
	
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

SiteCounts = open("DHch01_20nt_Ttrim_siteCount.txt")

lines = SiteCounts.readlines()

for i in range(len(lines)):
    lines[i] = to_query(lines[i])