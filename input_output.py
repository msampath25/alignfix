#deals with the input and output filetypes
#the they should be in this order: .fa and then .fq | we are going to be dealing with single end reads for this project
#the output will be a .sam file

input1 = open("input_fasta.fa", 'r').readlines()
input2 = open("input_fastq.fq", 'r').readlines()

output = open("output_sam.sam", 'w')
