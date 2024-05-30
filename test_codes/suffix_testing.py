from alignfix.suffix_arr import SA
import random
def generate_reads2(read_length=150, num_reads=50, fasta_file='/Users/manishsampath/Desktop/UCSD_Junior/CSE_185/final_project/alignfix/test_datasets/test2.fasta'):
    """
    Generates random reads from a given sequence in a FASTA file.

    Parameters:
    read_length (int): Length of each read to generate.
    num_reads (int): Number of reads to generate.
    fasta_file (str): Path to the FASTA file.

    Returns:
    list: A list of generated reads.
    """
    db = ''
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                continue
            else:
                db += line.strip()
    f.close()

    reads = []

    for i in range(num_reads):
        index = random.randint(0, int(len(db) - read_length + 1))
        read = db[index:index + read_length]
        reads.append(read)

    return reads


def errorProne(reads):
    """
    Introduces errors into the reads with a specified probability.

    Parameters:
    reads (list): A list of reads.
    chance_of_error (float): Probability of introducing an error at each nucleotide.

    Returns:
    list: A list of reads with errors introduced.
    """
    nucleotides = ["A", "C", "T", "G"]
    error_reads = []
    threshold = 95
    for read in reads:
        new_read =''
        for nc in read:
            chance = random.randint(0, 99)
            if chance > threshold:
                new_read += nucleotides[random.randint(0, 3)]
            else:
                new_read += nc
        error_reads.append(new_read)

    return error_reads


# Example usage:
# Generate random reads
reads = generate_reads2(read_length=150, num_reads=50, fasta_file='/Users/manishsampath/Desktop/UCSD_Junior/CSE_185/final_project/alignfix/test_datasets/test2.fasta')

# Introduce errors into the reads
error_reads = errorProne(reads)
with open('/Users/manishsampath/Desktop/UCSD_Junior/CSE_185/final_project/alignfix/test_datasets/reads2.fasta', 'w') as f:
    seq_count = 1
    for read in error_reads:
        f.write('>seq' + str(seq_count) + '\n')
        seq_count += 1
        f.write(read + '\n')
    f.close()





        
"""
def test_suffix_array():
    # Test case 1: Simple string
    db1 = "banana"
    sa1 = SA(db1)
    assert sa1.Seeds("ana") == (2, 3)
    assert sa1.Seeds("na") == (5, 6)
    assert sa1.Seeds("a") == (1, 3)

    # Test case 2: String with repeated characters
    db2 = "mississippi"
    sa2 = SA(db2)
    assert sa2.Seeds("iss") == (3, 4)
    assert sa2.Seeds("si") == (8, 9)
    assert sa2.Seeds("i") == (1, 4)
    
    # Test case 3: String with no matches
    db3 = "abcdefg"
    sa3 = SA(db3)

    assert sa3.Seeds("hij") == (-42, -69)
    assert sa3.Seeds("efh") == (-42, -69)
    
    # Test case 4: Empty string
    db4 = ""
    sa4 = SA(db4)
    assert sa4.Seeds("a") == (-42, -69)
    
    print("All test cases passed!")

test_suffix_array()


def additional_suffix_array_tests():
    # Case sensitivity
    db_case = "Banana"
    sa_case = SA(db_case)
    assert sa_case.Seeds("ana") == (1, 3)
    assert sa_case.Seeds("ANA") == (-42, -69)

    # Multiple non-contiguous positions
    db_multi = "abcabcabc"
    sa_multi = SA(db_multi)
    assert sa_multi.Seeds("abc") == (0, 3)
    assert sa_multi.Seeds("bc") == (1, 4)
    
    # Mixed cases and substrings
    db_mixed = "Mississippi"
    sa_mixed = SA(db_mixed)
    assert sa_mixed.Seeds("issi") == (2, 4)
    assert sa_mixed.Seeds("pi") == (9, 11)

additional_suffix_array_tests()
"""



