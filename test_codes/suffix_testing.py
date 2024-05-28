from suffix_arr import SA
import random

chance_of_error = random.randint(0.01,0.1)


def generate_reads1(read_length = 150, num_reads = 50):
    with open('test_datasets/test1.fasta', 'r') as file:
        lines = file.readlines()
        sequence = lines[1].strip()  # Get the second line which is the sequence
    reads = []
    sequence_length = len(sequence)
    for i in range(num_reads):
        start_index = random.randint(0, sequence_length - read_length)
        read = sequence[start_index:start_index + read_length]
        reads.append(read)
    return reads

def generate_reads2(read_length=150, num_reads=50):
    with open('test_datasets/test2.fasta', 'r') as file:
        lines = file.readlines()
        sequence = lines[1].strip()  # Get the second line which is the sequence
    reads = []
    sequence_length = len(sequence)
    for i in range(num_reads):
        start_index = random.randint(0, sequence_length - read_length)
        read = sequence[start_index:start_index + read_length]
        reads.append(read)
    return reads

def errorProne(reads):
    nucleotides = ["A","C","T","G"]
    error_reads = []
    for read in reads:
        new_read = []
        for nucleotide in read:
            if random.random() < chance_of_error:
                possible_errors = [n for n in nucleotides if n != nucleotide]
                new_nuc = random.choice(possible_errors)
                new_read.append(new_nucleotide)
            else:
                new_read.append(nucleotide)
        error_reads.append(''.join(new_read))
    return error_reads


reads1 = errorProne(generate_reads1())
reads2 = errorProne(generate_reads2())



        
        

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




