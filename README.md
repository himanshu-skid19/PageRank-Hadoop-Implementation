# PageRank Assignment

This is a simple implementation of the pagerank algorithm using hadoop as part of DA331: Big Data Analytics. 
## How to run

1. Install Python 3.x

2. Clone the repository

3. Run preprocess.py. This will generate ```extracted_graph.txt``` at your root directory

4. In WSL switch user to hadoop by running the command:

```bash
su - hadoop
```

5. run the command to start the hadoop cluster:

```bash
start-dfs.sh
```

6. run the command to check status of the hadoop cluster:

```bash
jps
```

7. If not made already, make the directories in HDFS:

```bash
hadoop fs -mkdir -p /home/hadoop/hadoopdata/hdfs/data
```

8. Copy the file to HDFS - do note that you will have to change the input path accordingly:

```bash
hadoop fs -put /mnt/c/Users/himan/Desktop/Dump/Hadoop/pagerank/extracted_graph.txt /home/hadoop/hadoopdata/hdfs/data
```
```

9. Remove the existing output directory if needed by running the command:

```bash
hadoop fs -rm -r /home/hadoop/hadoopdata/hdfs/output
```

10. copy the bash file and pagerank.py from windows to WSL - again change the path accordingly:

```bash
cp /mnt/c/Users/himan/Desktop/Dump/Hadoop/pagerank/pagerank.py ~/pagerank.py
cp /mnt/c/Users/himan/Desktop/Dump/Hadoop/pagerank/page_rank.sh ~/page_rank.sh

```

11. Convert pagerank.py and page_rank.sh to executables by running:

```
chmod +x ~/pagerank.py
chmod +x ~/page_rank.sh

```

12. Convert Windows Line Endings to Unix line Endings (if you edited your script in windwos, it might have Windwos-style line endings - '\r\n' which should be converted to Unix Style Line Endings - '\n')

```bash
dos2unix ~/pagerank.py
```

13. Run the bash script (you may modify the number of iterations as per your wish but here i have kept it at 10 iterations)
```bash
./pagerank.sh
```

14. Run the following command to view the output (following example is for iteration 10):
```bash
    hadoop fs -cat /home/hadoop/hadoopdata/hdfs/output/pagerank/iter10/part-*
```


15. Alternatively you may run the hadoop streaming Job for testing purposes:

```bash
hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar   -input /home/hadoop/hadoopdata/hdfs/data/extracted_graph.txt   -output /home/hadoop/hadoopdata/hdfs/output/   -mapper "python3 pagerank.py mapper"   -reducer "python3 pagerank.py reducer"
```





