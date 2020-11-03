import glob
import os
import sys

import time

import logging

import datetime
c1 = 0
count = 0

#Create and configure logger 
logging.basicConfig(filename="C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/cmd/RALogSearch/fileswithdate.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

path = sys.argv[1]

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
            dateonly = lastModifiedDate.strftime("%Y-%m-%d")
            # dateonly = datetime.strptime(lastModifiedDate, "%Y-%m-%d")
            print(dateonly)
                # logging.info("Removing.. %s ......... %s ......... %s", full_path, lastModifiedDate, sizeInBytes)
                # remove(full_path)