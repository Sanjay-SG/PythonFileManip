import glob
import os
import sys

# import time

import logging

import datetime

# from datetime import date
import re
# c1 = 0

now = datetime.datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string = now.strftime("%d%m%Y%H%M%S")

# print("date and time =", dt_string)	
regexlogfilename = "REGEXLOG"+dt_string

regexfilename = "REGEXMATCHES"+dt_string

#Create and configure logger 
# logging.basicConfig(filename="C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/cmd/RALogSearch/regex.log", 
logging.basicConfig(filename="C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/cmd/RALogSearch/"+regexlogfilename+".log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

path = sys.argv[1]

# path = sys.argv[1]
inputVar = sys.argv[2]

inputdate = sys.argv[3]
count1 = 0
count = 0
cnt1 = 0

filesArr = []


p1 = "ROUTEREQUEST/"+inputVar+"/[A-Z]{1}/E"

# regex = re.compile(r"ROUTEREQUEST/"+inputVar+"/[A-Z]{1}/E")
regex = re.compile(p1)

# pattern = "ROUTEREQUEST/"+inputVar+"/[A-Z]{1}/E"

print(inputVar)
print(p1)

# regexfilename = "REGEXMATCHES"+datetime.now()

fileLines = open(regexfilename,"w")


for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            stat = os.stat(full_path)
            
            # if stat.st_mtime <= time_in_secs:
                # sizeInBytes = os.path.getsize(path)
                # totalSizeInBytes = totalSizeInBytes + sizeInBytes
                # totalSize = totalSizeInBytes/(1024*1024*1024)
            t = os.path.getmtime(full_path)
            # lastModifiedDate = datetime.datetime.fromtimestamp(t)
            lastModifiedDate = datetime.datetime.fromtimestamp(t)
            dateonly = lastModifiedDate.strftime("%Y%m%d")
            # dateonly = datetime.strptime(lastModifiedDate, "%Y-%m-%d")
            # print(dateonly)
            # if(dateonly == "2020-10-28"):
            if(dateonly == inputdate):
                count1 = count1 + 1
                filesArr.append(os.path.join(root, file_))
for f1 in filesArr:
    # print(f1)
    file = open(f1, "r")
    data = file.read()
    with open(f1, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            # if pattern in line:
            result = re.search(regex, line)
                # return True
                # print(line )
            if(result != None):
                fileLines.write(str(line))
                cnt1 = cnt1 + 1
                logging.info("%s found in %s %d times.", result, file, cnt1)
    # logging.info("%s found in %s %d times.", pattern, file, data.count(pattern))
    # count = count + data.count("FNR Time: SK")
    # count = count + data.count(pattern)

# print("Total files selected: ",count1)
print("Matches: ", cnt1)

