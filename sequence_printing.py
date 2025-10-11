!pip install biopython

from Bio.Seq import Seq           #Seq is an object created using the following sequence

my_seq = Seq("AGTACACTGGTACGGACACGT")
my_seq
print("Sequence :", my_seq)

my_seq.complement()
print("Complementary sequence: ", my_seq.complement())

my_seq.reverse_complement()
print("Reverse complementary sequence: ", my_seq.reverse_complement())
