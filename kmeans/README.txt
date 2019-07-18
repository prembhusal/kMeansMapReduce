(to run the project java-1.8 or above should have been installed and hadoop 2.x should have been installed)

1.generate jar file from project (eg KMeans.jar)
either export jar from eclipse /or
 
or use following step to generate jar
a. create one folder and keep KMeans.java and CSVHelper.java
b. create KMeansClass directory and run the following command
export HADOOP_CLASSPATH=$(hadoop classpath)
javac -classpath ${HADOOP_CLASSPATH} -d 'path_to_KMeansClass' 'path_to_KMeans.java' 'path_to_CSVHelper.java'
jar -cvf KMeans.jar -C KMeansClass/ .

2.upload the centroids and data.hdfs file to HDFS
hadoop fs -put path_of_local_Centroids_file /HDFS_input_file_Path
hadoop fs -put path_of_local_data.hdfs_file /HDFS_input_file_Path

3.run KMeans.jar using the following command

hadoop jar KMeans.jar_file_location KMeans  /HDFS_input_file_Path /HDFS_output_file_path


-------------------------------
To run mapper.py
place centroids and data.hdfs file in same folder with mapper.py

then run 
cat centroids | python mapper.py
