import os
import sys

def IsLengthValid(stringValue, maxLength):
	return len(stringValue) == maxLength

def WriteContentsToFile(contents):
	# Opens a file in write mode
	# cleans up the content and replace with new if already exists
	# creates new file if it doesn't exist
	with open('Valid.txt', 'w') as f:
		for item in contents:
			f.write("%s\n" % item)


# Open the file in read mode with unsigned UTF text content
file = open("pyfile.txt","r", encoding='utf-8-sig')

# final build array
contentbuildarray = []

foundInvalidEntry = False
 
# run through each entry in the file lines
for each in file:	
	# split the line with tabspace which results in string array
	# rstrip removes the \n from end of each line
	splits = each.rstrip('\n').split('\t')

	# first word of the line split
	fileNo = splits[0]

	# next word of the line split
	ssn = splits[1]

	# check lengths
	fileNoLen = IsLengthValid(fileNo, 13)
	ssnLen = IsLengthValid(ssn, 9)
	
	# if any of these is not true, break
	if(fileNoLen != True or ssnLen != True):
		foundInvalidEntry = True
		break

	# join the valid ones
	delimitedValue =  ",".join([fileNo, ssn])

	# check if current line already exists
	exists = delimitedValue in contentbuildarray

	if(exists is not True):
		# if its new entry, add it to the array
		contentbuildarray.append(delimitedValue)

	

# close the file stream
file.close()

# check if an invalid entry is found
if(~foundInvalidEntry):
	# if not, start printing
		WriteContentsToFile(contentbuildarray)





