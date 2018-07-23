import os
import MySQLdb
import csv
from Bio import SeqIO
from Bio import motifs
from Bio.Alphabet import IUPAC
conn = MySQLdb.connect(host="localhost", user="root", passwd="MyNewPass", db="project_database")
cursor = conn.cursor()

# alignment_id MEDIUMTEXT, Gene_Symbol MEDIUMTEXT, seq_len MEDIUMTEXT, sequence MEDIUMTEXT


folder = 'C:/Users/Sasan Najar/Desktop/Echino_NEW/InternalBLAST/internalFas/'
fasta_output = open("fasta_output", "w")
alignment_id = 0
fasta_output.write("alignment_id" + '\t' + "Gene_Symbol" + '\t' + "seq_header" + '\t' + "seq_len" + '\t' + "sequence" + '\n')
for file_name in os.listdir(folder):
  if file_name.startswith('DDX'):
    print 'reading', file_name

  infile = open(folder+file_name, 'r')

  for record in SeqIO.parse(infile, 'fasta'):
      record_id = record.id
      seq = str(record.seq)
      # print("%s %i" % (record.id, len(record)))
      seq_len = len(record)-1
      alignment_id += 1


      #fasta_output.write(str(alignment_id) + '\t' + file_name + '\t' + record_id + '\t' + str(seq_len) + '\t' + seq + '\n')






      # sql_commad = 'INSERT INTO alignment (alignment_id, Gene_Symbol, seq_header, seq_len, sequence) values (alignment_id + "," file_name + "," + record_id + "," seq_len ","seq)'


  #     cursor.execute(sql_commad)
  #
  # conn.commit()
