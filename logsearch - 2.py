
# count = 0
'''
file = open('C:/Users/GunagiSa/OneDrive - Unisys/Desktop/SK/224/28/aircore_7.log', "r")
data = file.read()
count = data.count("FNR Time: SK")
# print(count)
'''

import glob
import os
import sys

import time

import logging

import datetime
c1 = 0
count = 0

#Create and configure logger 
logging.basicConfig(filename="C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/cmd/RALogSearch/logsearch.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

'''
# print(glob.glob("C:/Users/GunagiSa/OneDrive - Unisys/Desktop/SK/224/28/*.log"))
for root, dirs, files in os.walk("C:/Users/GunagiSa/OneDrive - Unisys/Desktop/SK/224/28/"):
    for filename in files:
        c1 = c1 + 1
        # print(filename)
        file = open(filename, "r")
        data = file.read()
        count = data.count("FNR Time: SK")
print(count)
print(c1)

'''


path = sys.argv[1]
pattern = sys.argv[2]

print(path)
print(pattern)
# path = 'C:/Users/GunagiSa/OneDrive - Unisys/Desktop/SK/224/28/'

files = []

fileLines = open("file.dat","a")
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.log' in file:
            files.append(os.path.join(r, file))
            # print(r)
            # print(d)

for f in files:
    # print(f)
    file = open(f, "r")
    data = file.read()
    with open(f, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if pattern in line:
                # return True
                # print(line )
                fileLines.write(line)
    logging.info("%s found in %s %d times.", pattern, file, data.count(pattern))
    # count = count + data.count("FNR Time: SK")
    count = count + data.count(pattern)
print(count)