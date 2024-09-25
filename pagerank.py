#!/usr/bin/env python3
import sys
import ast

n = 875713
damping_factor = 0.8  # PageRank damping factor

def mapper():
    for line in sys.stdin:
        key, value = line.split(": ")
        value_list = ast.literal_eval(value)
        page_rank = value_list[1]
        outlinks = value_list[2]
        if outlinks:
            for out in outlinks:
                print(f"{out}: {page_rank/len(outlinks)}")
        
        print(f"{key}: {value_list}")


def reducer():

    v = []
    current_key = None
    for line in sys.stdin:
        key, value = line.split(": ")
        try:
            val = float(value)
        except:
            val = ast.literal_eval(value)
        if current_key != key:
            if current_key == None:
                current_key = key
                v.append(val)
            else:
                outlink_list = []
                pagerank = 0
                for i in v:
                    if isinstance(i, list):
                        outlink_list = i[2]
                    else:
                        pagerank += i

                pagerank = (1 - damping_factor)/n + (damping_factor*pagerank)
                output = [current_key, pagerank, outlink_list]
                print(f"{current_key}: {output}")
            current_key = key
            v = [val]
        else:
            v.append(val)

    ## the last key
    if current_key is not None:

        outlink_list = []
        pagerank = 0
        for i in v:
            if isinstance(i, list):
                outlink_list = i[2]
            else:
                pagerank += i

        pagerank = (1 - damping_factor)/n + (damping_factor*pagerank)
        output = [current_key, pagerank, outlink_list]
        print(f"{current_key}: {output}")


if __name__ == "__main__":
    if sys.argv[1] == "mapper":
        mapper()
    elif sys.argv[1] == "reducer":
        reducer()