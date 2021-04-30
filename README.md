# Big-Data-Hadoop-MapReduce-Program-via-Hadoop-Streaming

For this project, I built a Hadoop MapReduce k-means clustering program from scratch using Hadoop’s Streaming API.

To do so, I orchestrated training iterations via a Bash script (run.sh) to pass data between my Python written mapper and reducer via STDIN and STDOUT.

I hypothesise that there are 8 clusters and write my Bash script to only run-up to a maximum number of iterations.

How to run the program (im my case):
3. reset Centroids.txt with datapoints from Centroids000000.txt (initalize cluster centroids)
2. move data file to hdfs
- hdfs dfs -copyFromLocal /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/data_points.txt /user/
3. run the bash file (Orchistrator)
- /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/run.sh

Files explained:
- Terminal Output
- commands run to execute map-reduce via terminal
- Centroids.txt
- started off as initial centroids and was updated each iteration. now it has the final centroid locations
-Centroids000000.txt
- randomly selected for datapoint from within the data that make up the initial centroid locations
- map_out_k8
- file containing cluster centroid updates for each of the 10 iterations
- Data Set (too large for Github)
- https://drive.google.com/drive/folders/1PMcgg7NxTQf3UXE0u3u4Gk0-FKNdXc_3?usp=sharing
