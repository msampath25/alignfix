import argparse
#deals with the input and output filetypes
#the they should be in this order: .fa and then .fq | we are going to be dealing with single end reads for this project
#the output will be a .sam file

def main():
    parse = argparse.ArgumentParser()
  
    parse.add_argument("referce_genome") #gets the fasta file that is the reference genome
    parse.add_argument("reads_file") #this gets the file with the reads
  
    args = parse.parse_args() #passes the arguments given by the user

    with open(args.reference_genome, "r") as f: #reads the file given by the user
        db = []
        for line in f:
            if not line.startswith(">") and line.strip().isalpha(): #if the line is not a header and made up of only letters
                db.append(line.strip()) #add the line to strings
              
    with open(args.reads_file, "r") as f: #reads the file given by the user
        reads = []
        for line in f:
            if not line.startswith(">") and line.strip().isalpha(): #if the line is not a header and made up of only letters
                reads.append(line.strip()) #add the line to strings

