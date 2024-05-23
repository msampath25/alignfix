import argparse

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


    __outputFile__(args)
    return 0


                
if __name__ == "__main__":
    main()
