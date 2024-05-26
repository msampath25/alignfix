import argparse
import numpy as np
from suffix_arr import SA
from alignment import Alignment

def __outputFile__(args):
    sam_file = open(args.output, "w")
    with open(args.genome, "r") as f:
        seq_length = 0
        for line in f:
            if line.startswith(">"):
                if seq_length > 0:
                    sam_file.write(f"@SQ\tSN:{seq_name}\tLN:{seq_length}\n")
                    seq_length = 0
                seq_name = line.strip().split(">")[1]
            else:
                seq_length += len(line.strip())
        if seq_length > 0:
            sam_file.write(f"@SQ\tSN:{seq_name}\tLN:{seq_length}\n")

    # Write @HD and @PG headers
    sam_file.write("@HD\tVN:1.5\tSO:unsorted\tGO:query\n")
    sam_file.write(f"@PG\tID:bwa\tPN:bwa\tVN:0.7.17-r1198-dirty\tCL:bwa mem {args.reference_genome} {args.reads_file}\n")

    # Write alignment records
    with open(args.reads_file, "r") as f:
        read_id = ""
        sequence = ""
        line_num = 1
        for line in f:
            if (line_num - 1) % 4 == 0:
                if read_id:
                    # Write previous alignment record
                    sam_file.write(f"{read_id[:-2]} More data goes here\n") # """Write output here"""
                read_id = line.strip().split("@")[1]
            elif len(line.strip()) > 0 and not line.startswith("+"):
                if not sequence:
                    sequence = line.strip()
            line_num += 1

        # Write the last alignment record
        if read_id:
            sam_file.write(f"{read_id[-2]} More data goes here\n") # """Write output here"""

    sam_file.close()
def extractQueries(file):
    queries = np.empty(dtype = 'object')
    with open(file, "r") as f:
        for line in f:
            queries.append(line.strip())
    return queries

def extractDatabase(file):
    database = ''
    with open(file, "r") as f:
        for line in f:
            database += line.strip()
    return database
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

    queries = extractQueries(args.query)
    database = extractDatabase(args.genome)

    #The shifted seed might be wrong tbh. Someone else debug it

    for query in queries:
        for i in range(0, len(query) - 15 + 1):
            if exit:
                break
            sa = SA(database)
            seeds = sa.Seeds(query)
            # write some basic checks that the seed actually exists
            if seeds:
                exit = True
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
            if best_alignment:
                query_name = query
                ref_name = args.genome.split('/')[-1]
                position = best_alignment[0]
                sequence = query
                alignment_record = write_alignment_record(query_name, ref_name, position, sequence)
                alignments.append(alignment_record)
        
def write_alignment_record(sam_file, query_name, ref_name, position, sequence):
    mapping_quality = 255 #default
    cigar_string = "*"
    alignment_str = f"{query_name}\t0\t{ref_name}\t{position}\t{mapping_quality}\t{cigar_string}\t*\t0\t0\t{sequence}\t*\n"
    sam_file.write(alignment.str)





    __outputFile__(args)
    return 0


                
if __name__ == "__main__":
    main()
