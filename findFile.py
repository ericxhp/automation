import os
import sys
import linecache

returnList = []

def search_file_in_dir(fileName, dirName):

    global returnList
    fileList = [x for x in os.listdir(dirName) if os.path.isfile(os.path.join(dirName,x))]
    dirList = [i for i in os.listdir(dirName) if os.path.isdir(os.path.join(dirName,i))]
    if fileName in fileList:
    	returnList.append(os.path.join(dirName, fileName))
    dirListLen = len(dirList)
    if dirListLen > 0:
    	for d in dirList:
    		search_file_in_dir(fileName, os.path.join(dirName, d))
    print returnList
    return returnList

def parse_file(file_name):
	keywords_1 = '@feature:'
	keywords_2 = '@owner:'
	splitFlag = ':'
	
	lines = linecache.getlines(file_name)[0:300]
	for line in lines:
		strline = ('').join(line)
		nPos_1 = strline.find(keywords_1)
		nPos_2 = strline.find(keywords_2)
		if nPos_1 == 0:
			result = strline.split(splitFlag)
			tc_feature = result[1]
			print tc_feature		
		if nPos_2 == 0:
			result_2 = strline.split(splitFlag)
			tc_owner = result_2[1]
			print tc_owner

if __name__ == "__main__":     
	
	filePath = search_file_in_dir('MP_ModeSelect_AllChangeableForThreePage_20.py', 'C:\Work\Test_Case_Development\UFS\master\HostCase')
	parse_file(filePath[-1])

