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
    keywords_1 = r'@feature: (.*)'
    keywords_2 = r'@owner: (.*)'
    
    lines = linecache.getlines(file_name)[0:300]
    for line in lines:
        match_feature = re.match(keywords_1,line)
        match_owner = re.match(keywords_2,line)
        if match_feature:
            feature = match_feature.group(1)        
            print feature
        
        if match_owner:
            owner = match_owner.group(1)
            print owner

if __name__ == "__main__":     
	
	filePath = search_file_in_dir('MP_ModeSelect_AllChangeableForThreePage_20.py', 'C:\Work\Test_Case_Development\UFS\master\HostCase')
	parse_file(filePath[-1])

