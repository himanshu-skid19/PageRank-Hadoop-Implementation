import sys
import os
from collections import defaultdict


def preprocess_graph(file_path):
    graph = defaultdict(lambda: [None, 0, []])
    num_nodes = 875713
    with open(file_path, 'r') as f:
        for line in f:
            from_node, to_node = map(int, line.split())
            if graph[from_node][0] is None:
                graph[from_node][0] = from_node
                graph[from_node][1] = 1/num_nodes
            graph[from_node][2].append(to_node)
    return graph 

def save_graph_to_file(graph, output_file):
    with open(output_file, 'w') as f:
        for key, value in graph.items():
            f.write(f"{key}: {value}\n")  # Write each entry as "key: value"

if __name__ == "__main__":
    file_path = 'C:/Users/himan/Desktop/Dump/Hadoop/pagerank/web-Google.txt'
    output_file = 'C:/Users/himan/Desktop/Dump/Hadoop/pagerank/extracted_graph.txt'
    graph= preprocess_graph(file_path)
    save_graph_to_file(graph, output_file) 