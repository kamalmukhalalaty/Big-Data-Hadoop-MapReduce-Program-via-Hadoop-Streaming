# Big-Data-Hadoop-MapReduce-Program-via-Hadoop-Streaming

How to run:

1- move data file to hfs
hdfs dfs -copyFromLocal /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/data_points.txt  /user/

2- run it 
/Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/run.sh

3- you don’t actually need to make these changes if u already ran it for k4. I wrote the code in such a way where the amount of initial centroids you give it tells it how many clusters to look for. so as long as the centroids.txt file path is changed in the bash file the program will run as needed. 

Files explained:

- Terminal Output
  - commands run to execute map reduce on terminal
- Centroids.txt
  - started off as initial centroids and was updated each iteration. now it has the final centroid locations
-Centroids000000.txt
  - randomly selected for datapoint from within the data that make up the initial centroid locations
- map_out_k8
  - file containing cluster centroid updates for each of the 10 iterations
