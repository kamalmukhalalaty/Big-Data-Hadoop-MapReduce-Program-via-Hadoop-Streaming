#!/usr/bin/env python3
#REDUCER
from __future__ import print_function
import sys

def calculateNewCentroids():
    current_centroid = None
    sum_x = 0
    sum_y = 0
    count = 0

    # input comes from STDIN
    for line in sys.stdin:            # For each line 

        # collect input key value pairs from mapper
        centroid_index, x, y = line.split('\t')   # printed with tabs to seperate now use that to get the data
        # convert x and y (currently a string) to float
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            # float was not a number so ignore this line
            continue

        # this only works because Hadoop sorts map output by key (centriod label) before it is passed to the reducer
        # so the lines we are looping through are already sorted eg. block belonging to each centriod 
        if current_centroid == centroid_index: 
            count += 1
            sum_x += x
            sum_y += y
        else:
            if count != 0:
                # print the average of that cluster to get its new centroid location
                print(str(sum_x / count) + ", " + str(sum_y / count))

            # first iter goes/starts here and the reset for different block of centriod starts here
            current_centroid = centroid_index                       # set current centriod to first centroid passed
            sum_x = x
            sum_y = y
            count = 1
    
    # print last cluster's centroids as we exit the above loop without computing it for the final block
    if current_centroid == centroid_index and count != 0:         
        print(str(sum_x / count) + ", " + str(sum_y / count))

if __name__ == "__main__":
  calculateNewCentroids()
"""
prints 3 new centered centriods
"""