'''
Created on June 4, 2014

@author: Lixin
'''
import os, sys

if __name__=="__main__":
    argumentLen = len(sys.argv)
    filePath = ''
    if argumentLen >= 2:
        filePath = os.path.abspath(sys.argv[1])
    else:
        print 'Input file path please'
        sys.exit(1)
    
    if not os.path.exists(filePath):
        print 'cannot find file: %s' %filePath
        sys.exit(1)
    pre_name = os.path.basename(filePath).split(".")[0]
    os.mkdir(pre_name)
    out_path = os.path.abspath(pre_name)
    output = out_path + "//"+ pre_name +'_{0}.log'
    index = 0
    f = open(filePath)
    maxCount = int(sys.argv[2])
    lines = []
    count = 1
    while True:    
        line = f.readline()
        if line:
            lines.append(line)
            count += 1
            if count >= maxCount:
                outFile = output.format(index)
                outFile = os.path.abspath(outFile)
                o = open(outFile, 'w')
                o.writelines(lines)
                o.close()
                index += 1
                del lines[0:len(lines)]
                count = 1
        else:
            outFile = output.format(index)
            outFile = os.path.abspath(outFile)
            o = open(outFile, 'w')
            o.writelines(lines)
            o.close()
            index += 1
            del lines[0:len(lines)]
            break
            
