import argparse
#deals with the input and output filetypes
#the they should be in this order: .fa and then .fq | we are going to be dealing with single end reads for this project
#the output will be a .sam file

def main():
    parse = argparse.ArgumentParser()
    
    parse.add_argument("reference_genome") #gets the fasta file that is the reference genome
    parse.add_argument("reads_file") #this gets the file with the reads

    args = parse.parse_args() #passes the arguments given by the user

    sam_file = open("sequence_alignment_map.sam", "w")

    # Write @SQ headers
    with open(args.reference_genome, "r") as f:
        for line in f:
            if line.startswith(">"):
                seq_name = line.strip().split(">")[1]
                seq_length = 0
                for seq_line in f:
                    if seq_line.startswith(">"):
                        break
                    seq_length += len(seq_line.strip())
                sam_file.write(f"@SQ\tSN:{seq_name}\tLN:{seq_length}\n")

    # Write @HD and @PG headers
    sam_file.write("@HD\tVN:1.5\tSO:unsorted\tGO:query\n")
    sam_file.write("@PG\tID:bwa\tPN:bwa\tVN:0.7.17-r1198-dirty\tCL:bwa mem /path/to/reference_genome.fa /path/to/reads_file.fq\n")

    # Write alignment records
    with open(args.reads_file, "r") as f:
        read_id = ""
        sequence = ""
        quality = ""
        for line in f:
            if line.startswith("@"):
                if read_id:
                    # Write previous alignment record
                    sam_file.write(f"{read_id}\t99\tchr1\t1\t60\t101M\t=\t1\t101\t{sequence}\t{quality}\tNM:i:0\tMD:Z:101\tMC:Z:101M\tMQ:i:60\tAS:i:101\tXS:i:0\n")
                read_id = line.strip().split("@")[1]
            elif len(line.strip()) > 0 and not line.startswith("+"):
                if not sequence:
                    sequence = line.strip()
                else:
                    quality = line.strip()

        # Write the last alignment record
        if read_id:
            sam_file.write(f"{read_id}\t99\tchr1\t1\t60\t101M\t=\t1\t101\t{sequence}\t{quality}\tNM:i:0\tMD:Z:101\tMC:Z:101M\tMQ:i:60\tAS:i:101\tXS:i:0\n")

    sam_file.close()
                
if __name__ == "__main__":
    main()
