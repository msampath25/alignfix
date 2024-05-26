# alignfix

Version: 0.1

Alignfix is a tool for aligning short Illumina reads to a genome based on a seed and extend method.
Alignifx uses fast pattern matching to rapidly find seeds in a genome and then proceeds to align the reads 
in the genome located around the seed. Alignfix consists of two key algorithmic ideas. For generating seeds,
Alignfix uses fast pattern matching by way of preprocessing the genome into suffix arrays. With a seed, alignfix creates
two different alignment on either side of the seed. Alignfix uses affine gap penalties for the alignment scoring
function. 

Friday May-24 (Just a placeholder for right now)
## basic usage:

The `SA` class creates a suffix array for a given database or genome string. It provides methods to find the first and last occurrences of a pattern (seed) within the suffix array.
We have yet to create a command line usage for our project, so you will have to use the code below as a guideline.

### Initializing the Suffix Array and Searching for Patterns

```python
from sa import SA

# Create a suffix array for the database 'ACGT'
suffix_array = SA('ACGT')

# Search for seeds using Seeds method
seeds = suffix_array.Seeds('GT')
```

## Command Line Arguments

- `--genome`, `-g`: Fasta format of genome
- `--query`, `q`: Fasta format of queries
- `--output`, `-o`: File path for alignment output