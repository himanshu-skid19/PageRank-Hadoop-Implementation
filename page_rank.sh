#!/bin/bash

INPUT_DIR=/home/hadoop/hadoopdata/hdfs/data/extracted_graph.txt
OUTPUT_DIR_BASE=/home/hadoop/hadoopdata/hdfs/output/pagerank 
NUM_ITERATIONS=10

hadoop fs -rm -r $OUTPUT_DIR_BASE

# Initialize input for the first iteration
OUTPUT_DIR=$OUTPUT_DIR_BASE/iter0
hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input $INPUT_DIR \
  -output $OUTPUT_DIR \
  -mapper "python3 pagerank.py mapper" \
  -reducer "python3 pagerank.py reducer"

# Loop for running iterations
for ((i=1; i<NUM_ITERATIONS; i++))
do
    INPUT_DIR=$OUTPUT_DIR
    OUTPUT_DIR=$OUTPUT_DIR_BASE/iter$i
    
    hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar  \
      -input $INPUT_DIR \
      -output $OUTPUT_DIR \
      -mapper "python3 pagerank.py mapper" \
      -reducer "python3 pagerank.py reducer"

    previous_output=$OUTPUT_DIR
done
