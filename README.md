# alignfix (CSE 185 Project)

Version: 0.1

Alignfix is a tool for aligning short Illumina reads to a genome based on a seed and extend method.
Alignifx uses fast pattern matching to rapidly find seeds in a genome and then proceeds to align the reads 
in the genome located around the seed. Alignfix consists of two key algorithmic ideas. For generating seeds,
Alignfix uses fast pattern matching by way of preprocessing the genome into suffix arrays. With a seed, alignfix creates
two different alignment on either side of the seed. Alignfix uses affine gap penalties for the alignment scoring
function.

## Install instructions
Installation requires the NumPy and Pyfaidx library. You must have Python 3.7 or later versions to install NumPy and Python 3.6 or later versions to install Pyfaidx.
You can install these libraries using the following command:
```
pip install numpy
```
```
pip install pyfaidx
```
Navigate to the directory in which you would like to download this tool and use the following command:
```
git clone https://github.com/msampath25/alignfix
```
Change into that directory and install the tool so that it can be used from the command line. You can install ```alignfix``` with the following command:
```
cd alignfix
```
Once required libraries are installed, you can install ```alignfix``` with the following command: 
```
python setup.py install
```
Note: if you do not have root access, you can run the commands above with additional options to install locally:
```
python setup.py install --user
```
If your operating system is Unix, then run ```chmod +x alignfix.py```.
If the install was successful, typing ```alignfix --help``` should show a useful message. 

## Mandatory Command Line Arguments
- `--genome`, `-g`: Fasta format of genome
- `--query`, `-q`: Fasta format of queries
- `--output`, `-o`: File path for alignment output

## basic usage:
```unix
alignfix --genome req1 --query req2 --output req3
```
### Ex:
```unix
alignfix --genome test_datasets/test1.fasta --query test_datasets/small_queries_test.fasta --output test_output.txt
```
