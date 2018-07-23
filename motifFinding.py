import os
import re
import MySQLdb
import csv
from Bio import SeqIO
from Bio import motifs
from Bio.Alphabet import IUPAC
conn = MySQLdb.connect(host="localhost", user="root", passwd="MyNewPass", db="project_database")
cursor = conn.cursor()

# alignment_id MEDIUMTEXT, Gene_Symbol MEDIUMTEXT, seq_len MEDIUMTEXT, sequence MEDIUMTEXT


folder = 'C:/Users/Sasan Najar/Desktop/Echino_NEW/Ready4MSAInternal/'
motif_output = open("DEADBOX_output", "w")

motif_output.write("entry_id" + '\t' + "file_name" + '\t' + "seq_id" + '\t' + "DEAD_BOX_start_Pos" + '\t' + "DEAD_BOX_end_pos" + '\n')

entry_id = 0;
for file_name in os.listdir(folder):
  if file_name.endswith('_MSA'):
    print 'reading', file_name

    infile = open(folder+file_name, 'r')
    for record in SeqIO.parse(infile, 'fasta'):
      record_id = record.id
      seq = str(record.seq)

      # # print("%s %i" % (record.id, len(record)))
      # seq_len = len(record)-1
      # print seq
      pattern=re.compile(r"(D[A-Z]{2}[D])")
      for m in pattern.finditer(seq):
        print m.start(), m.end()


      s=re.findall(pattern,seq)
      mas = re.match(pattern, seq)
      # print '%s:%s' %(seq,s) , len(s)
      # Startend = [(a.start(), a.end()) for a in list(re.finditer('DEAD', seq))]
      # seqtemp = "DEADLPOIURYHNDJDNCC"

      for a in list(re.finditer("DEAD", seq)):
        startpos = a.start()+1
        endpos = a.end()+1
        # print record_id, startpos, endpos
        entry_id += 1

        motif_output.write(str(entry_id) + '\t' + file_name + '\t' + record_id + '\t' + str(startpos) + '\t' + str(endpos) + '\n')









