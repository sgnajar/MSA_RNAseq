# from __future__ import print_function
import os
import MySQLdb
import csv
from Bio import SeqIO

# connect to the database by adding hostname, username, password and the databasename
conn = MySQLdb.connect(host="localhost", user="root", passwd="MyNewPass", db="db_classproject")
cursor = conn.cursor()



folder = 'C:/Users/Sasan Najar/Desktop/Echino_NEW/InternalBLAST_mafft_out/'

entry_id = 0

for file_name in os.listdir(folder):
  if file_name.endswith('mafft'):
    print 'reading', file_name
    infile = open(folder+file_name, 'r')
    for record in SeqIO.parse(infile, 'fasta'):

      record_id = record.id
      seq = str(record.seq)

      entry_id += 1

      sql_commad = 'INSERT INTO alignment_big (entry_id, file_name, seq_header'
      for i in xrange(len(seq)):
        if i<940:
          sql_commad += ' , pos_' + str(i)
      sql_commad += ') values (' + str(entry_id) + ', "' + file_name+ '", "' + record_id + '" '
      for i in xrange(len(seq)):
        if i<940:
          sql_commad += ' , "' + seq[i] + '"'
      sql_commad += ')'

      cursor.execute(sql_commad)

  conn.commit()

  #loop across columns postions for a group(File)
  #look for consecutive counts that high that have "D" followed by "E A D"







# headerList = []
# seqList = []
#
# infile = open("test3.txt", 'r')
# out = open("out_test.txt", 'w')
#
# for record in SeqIO.parse(infile, 'fasta'):
#   headerList.append(record.id)
#   seqList.append(str(record.seq))
#
# # print (*seqList, sep = '\n')
# print len(seqList)
#
# for line_no in xrange(len(seqList)):
#   print
#   for char_no in range(len(seqList[line_no])):
#     print seqList[line_no][char_no],
#




# for i in str(len(seqList)):
#   # print (seqList[i])
#   for seq in seqList:
#       charList = list(seq)
#       print charList
#       #insert to db



# for index,item in enumerate(seqList):
#   print 'Seq', index+1, '--', item
#     for ...

# with open("test2.txt") as f:
#   while True:
#     c = f.readline(1)
#     if not c:
#       print "end"
#       break
#     print "read a character", c
