import argparse
import numpy as np
from suffix_arr import SA
from alignment import Alignment
from pyfaidx import Fasta

def extractDatabase(file):
    database = ''
    with open(file, "r") as f:
        for line in f:
            if '>' in line:
                continue
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

    # Setting up parser -> this can stay here
    parser = argparse.ArgumentParser(prog='alignfix', description='A seed and extends aligner.\n\nThis program aligns queries against a genome using a seed-and-extend approach. It takes a genome file, a query file, and produces an output file with the alignments.')
    parser.add_argument('-g', '--genome', help='Path to the genome file')
    parser.add_argument('-q', '--query', help='Path to the query file')
    parser.add_argument('-o', '--output', help='Path to the output file')
    args = parser.parse_args()

    # Check if the required arguments are provided
    if not args.genome or not args.query or not args.output:
        parser.print_help()
        return 1
    
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

        seeds = None
        for i in range(0, len(queries[query]) - 15 + 1):
            sa = SA(database)
            print('These are the l-mer matches we are looking for: ')
            print(str(queries[query][i:i + 15]))
            seeds = sa.Seeds(str(queries[query][i:i + 15]))
            # write some basic checks that the seed actually exists
            if -42 in seeds and -69 in seeds:
                continue
            else:
                break

        #Checking to see if some lmer exists
        if seeds is None:
            write_failure(args.output, query_name)
            continue

        #Calculating the optimal alignment given our set of seeds
        max_score = -9999
        best_alignment = None
        for seed in seeds:
            r = int(len(queries[query]) + 50)
            if seed - (r//2) < 0:
                db_small = database[:int(seed + (r//2))]
                shifted_seed = int(seed)
            else:
                db_small = database[int(seed - (r // 2)) : int(seed + (r // 2))]
                shifted_seed = int(len(db_small) - (r // 2))
            l = 15
            a = Alignment(db_small, str(queries[query]), shifted_seed, l, r)
            results = a.Align()
            if results[0] > max_score:
                best_alignment = results

        #We want to write to file when we have found the optimal alignment
        print("Finished " + str(query_count) + " queries")
        if best_alignment is not None:
            query_name = query
            write_alignment(args.output, query_name, best_alignment)
            query_name = ''
            best_alignment = None
        else:
            write_failure(args.output, query_name)

    return 0
                
if __name__ == "__main__":
    main()
