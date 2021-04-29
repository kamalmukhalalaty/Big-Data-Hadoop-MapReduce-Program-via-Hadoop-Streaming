#!/usr/bin/env python3

#MAPPER
from __future__ import print_function
import sys
from math import sqrt

# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
    centroids = []
    with open(filepath) as fp:       # this part of the code was taken from github dont understand what it does
        line = fp.readline()
        while line:
            if line:
                try:
            	    line = line.strip()
            	    mu = line.split(', ')       # this is the format in which i wrote my centriod in the file
                    # mu[0] is the x1 and mu[1] is x2 point of a centroid
            	    centroids.append([float(mu[0]), float(mu[1])])
                  
                except:
                    break
            else:
                break
            line = fp.readline()
    fp.close()
    # print(centroids)
    return centroids

# create clusters based on initial centroids
def createClusters(centroids):
    
    for line in sys.stdin.readlines():             # for every row of the dataset # reading from stdin
        # print('open')         
        line = line.strip()
        x = line.split(',')
        # print(line)
        min_dist = 100000000000000     # positive infinity
        index = -123                   # random initalization
        for centroid in centroids:     # for every centroid  
            try:
                x[0] = float(x[0])         # convert stdin string to text
                x[1] = float(x[1])
                # print(x)
            except ValueError:
              	# float was not a number, so ignore this line
              	continue
                            
            # print(x)
            current_dist = sqrt(pow(x[0] - centroid[0], 2) + pow(x[1] - centroid[1], 2)) # L2 Norm from data datapoint to centriod
            # find the centroid which is closer to the point
            # print(current_dist)
            if current_dist <= min_dist:
                min_dist = current_dist
                index = centroids.index(centroid) # get the index of closest distance centroid and save it as index
                            
        print("{}\t{}\t{}".format(index, x[0], x[1]))  # as needed outputing key value pair consisting of cluster label and corr dpoint
                
if __name__ == "__main__":
	centroids = getCentroids('/Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_4/centroids.txt')
	createClusters(centroids)
'''
outputs key value pair consisting of asigned cluster label and datapoint
'''