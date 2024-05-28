# alignfix

Version: 0.1

Alignfix is a tool for aligning short Illumina reads to a genome based on a seed and extend method.
Alignifx uses fast pattern matching to rapidly find seeds in a genome and then proceeds to align the reads 
in the genome located around the seed. Alignfix consists of two key algorithmic ideas. For generating seeds,
Alignfix uses fast pattern matching by way of preprocessing the genome into suffix arrays. With a seed, alignfix creates
two different alignment on either side of the seed. Alignfix uses affine gap penalties for the alignment scoring
function.

## Install instructions
Installation requires the Numpy library.

## Mandatory Command Line Arguments
- `--genome`, `-g`: Fasta format of genome
- `--query`, `q`: Fasta format of queries
- `--output`, `-o`: File path for alignment output

## basic usage:
```unix
alignfix --genome req1 --query req2 --output req3
```
### Ex:
```unix
alignfix --genome test_datasets/test1.fasta --query test_datasets/small_queries_test.fasta --output test_output.txt
```
