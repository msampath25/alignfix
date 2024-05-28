import argparse
import numpy as np
from suffix_arr import SA
from alignment import Alignment
from pyfaidx import Fasta

def extractDatabase(file):
    database = ''
    with open(file, "r") as f:
        for line in f:
            database += line.strip()
    return database
def write_alignment(o_file, name, alignment):
    with open(o_file, "a") as f:
        f.write(">" + name + "\n")
        f.write(alignment[2] + "\n")
        f.write(alignment[1] + "\n")
        f.write("Score: " + str(alignment[0]) + "\n")
    f.close()
    return
def write_failure(o_file, name):
    with open(o_file, "a") as f:
        f.write(">" + name + "\n")
        f.write("Query not found!!")
        f.write("Query not found!!")
        f.write("Score: " + str(-1) + "\n")
    f.close()
    return

def main():
    """
     for each query in the query file
        create a suffix array and find seeds
        for each seed
            compute an alignment
            keep track of highest scoring alignment
        store optimal alignment and its score
     output the alignment to some file
    """

    #Setting up parser -> this can stay here
    parser = argparse.ArgumentParser(prog='alignfix', description='A seed and extends aligner')
    parser.add_argument('-g', '--genome')
    parser.add_argument('-q', '--query')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

    # reading in the queries and database here
    # queries is a list of patterns
    # database is one long string
    queries = Fasta(args.query)
    database = extractDatabase(args.genome)

    #The shifted seed might be wrong tbh. Someone else debug it
    # the case that no lmer of size 15 shows up
    query_count = 0
    for query in queries.keys():
        query_count += 1
        for i in range(0, len(queries[query]) - 15 + 1):
            # we only want one seed per query, but we need to make sure that it does in fact exist
            if exit:
                break
            sa = SA(database)
            seeds = sa.Seeds(queries[query][i:i + 15])
            # write some basic checks that the seed actually exists
            if not -42 in seeds or not -69 in seeds:
                exit = True
            else:
                continue
            max_score = -9999
            best_alignment = None
            for seed in seeds:
                if seed - 100 < 0:
                    db_small = database[:seed + 100]
                    shifted_seed = seed
                else:
                    db_small = database[seed - 100 : seed + 100]
                    shifted_seed = len(db_small) - 100
                l = 15
                r = 200
                a = Alignment(db_small, shifted_seed, l, r)
                results = a.Align()
                if results[1] > max_score:
                    best_alignment = results
            print("Finished " + str(query_count) + " queries")
            if best_alignment is not None:
                query_name = query
                write_alignment(args.output, query_name, best_alignment)
            else:
                write_failure(args.output, query_name)


    return 0


                
if __name__ == "__main__":
    main()
