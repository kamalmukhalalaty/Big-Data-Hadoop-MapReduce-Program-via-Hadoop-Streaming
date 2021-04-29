#!/bin/bash
i=1

cd /usr/local/Cellar/hadoop/3.3.0/libexec
export HADOOP_HOME=
cd /usr/local/Cellar/hadoop/3.3.0/libexec

while((i <= 10))  
do

  bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/mapper.py    -mapper /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/mapper.py  -file /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/reducer.py      -reducer /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/reducer.py  -numReduceTasks 1 -input /user/data_points.txt                          -output /user/map_out_k8/clusterz$i    

  rm  /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/centroids.txt
  hdfs dfs -copyToLocal /user/map_out_k8/clusterz$i/part-00000 /Users/kamalal-mukhalalaty/Desktop/Kmeans_Assignment_1/K_means/K_8/centroids.txt
	
  i=$((i+1))
done

cd 