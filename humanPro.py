from Bio import SeqIO
import sys

file = raw_input("Insert your fasta file to parse: ")
#input_file = open(file, "r")

fasta_sequences = SeqIO.parse(open(file), 'fasta')
# with open (file , 'r') as f:
#     read_data = f.read()
#     print read_data

for record in fasta_sequences:
  print record.id, len(record)

for fasta in fasta_sequences:
  name, sequence = fasta.id, str(fasta.seq)
  # new_sequence = some_function(sequence)

  # print name

  # print sequence

  # print len(sequence)
  #
  # print fasta.description



