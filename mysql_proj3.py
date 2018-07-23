#!/usr/bin/python
import MySQLdb
import csv
from Bio import SeqIO

# connect to the database by adding hostname, username, password and the databasename
conn = MySQLdb.connect(host="localhost", user="root", passwd="MyNewPass", db="db_classproject")
cursor = conn.cursor()

#create a table 1
cursor.execute("CREATE TABLE metadatagene (tax_id MEDIUMTEXT NOT NULL, Org_name MEDIUMTEXT NOT NULL, GeneID MEDIUMTEXT NOT NULL, CurrentID MEDIUMTEXT NOT NULL, Status MEDIUMTEXT , Gene_Symbol varchar(45), Aliases MEDIUMTEXT, description MEDIUMTEXT, other_designations MEDIUMTEXT, map_location MEDIUMTEXT, chromosome MEDIUMTEXT, genomic_nucleotide_accession MEDIUMTEXT, start_position_on_the_genomic_accession MEDIUMTEXT ,end_position_on_the_genomic_accession text, orientation text, exon_count text, OMIM text)")
conn.commit()

#open the metadata file
file1 = open('C:/Users/Sasan Najar/Desktop/gene_result_humandeadbox_metadata.csv')
csv_data = csv.reader(file1)

# for row in csv_data:
#    print row

#read through the file and insert each row into the table
firstline = True
for row in csv_data:
    if firstline:    #skip first line
          firstline = False
          continue
    cursor.execute("INSERT INTO metadatagene (tax_id, Org_name, GeneID, CurrentID, status, Gene_Symbol, Aliases, description, other_designations, map_location, chromosome, genomic_nucleotide_accession, start_position_on_the_genomic_accession, end_position_on_the_genomic_accession, orientation, exon_count, OMIM) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()

# -----create table2
cursor.execute("CREATE TABLE HumanProtein (accession_id MEDIUMTEXT, entry_name MEDIUMTEXT, protein_name MEDIUMTEXT, org_name MEDIUMTEXT, Gene_Symbol varchar(45), sequence text, seq_len MEDIUMTEXT)")
conn.commit()

#open the humanprotein file
file2 = open('C:/Users/Sasan Najar/Desktop/HumanProtein.csv')
csv_data2 = csv.reader(file2)

# for row in csv_data2:
#     print(row)

#read through the file and insert each row into the table
firstline = True
for row in csv_data2:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO HumanProtein (accession_id, entry_name, protein_name, org_name, Gene_Symbol, sequence, seq_len) VALUES (%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()

#-----create table3
cursor.execute("CREATE TABLE blastoutput (blast_program MEDIUMTEXT, Gene_Symbol varchar(45), query_id MEDIUMTEXT, query_def MEDIUMTEXT, query_len MEDIUMTEXT)")
conn.commit()

#open the blast_output file
file3 = open('C:/Users/Sasan Najar/Desktop/Blastoutput_table.csv')
csv_data3 = csv.reader(file3)

for row in csv_data3:
    print(row)

#read through the file and insert each row into the table
firstline = True
for row in csv_data3:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blastoutput (blast_program, Gene_Symbol, query_id, query_def, query_len) VALUES (%s,%s,%s,%s,%s)", row)
conn.commit()


# -----create table4
cursor.execute("CREATE TABLE blast_parameter (Gene_Symbol varchar(45), query_id MEDIUMTEXT, matrix_type MEDIUMTEXT, gap_open MEDIUMTEXT, gap_extend MEDIUMTEXT)")
conn.commit()
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX1','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX2A','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX2B','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX3X','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX3Y','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX4','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX5','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX6','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX10','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX17','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX18','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX19A','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX19B','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX20','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX21','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX23','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX24','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX25','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX27','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX28','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX31','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX39A','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX39B','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX41','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX42','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX43','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX46','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX47','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX48','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX49','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX50','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX51','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX52','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX53','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX54','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX55','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX56','Query_1', 'BLOSUM62', '11', '1')")
cursor.execute("INSERT INTO blast_parameter (Gene_Symbol, query_id, matrix_type, gap_open, gap_extend) VALUES ('DDX59','Query_1', 'BLOSUM62', '11', '1')")
conn.commit()

# -----create table5-----------------------------------------------------------------------------------------------------
cursor.execute("CREATE TABLE blast_hit (Gene_Symbol varchar(45), query_id varchar(45), hit_num MEDIUMTEXT, hit_id MEDIUMTEXT, hit_accession MEDIUMTEXT, hit_len MEDIUMTEXT)")
conn.commit()
#
# #open the hit files--------------------------------------------------------------------------------------------------------
hit_file1 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX1_hit_output')
hit_file2 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX2A_hit_output')
hit_file3 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX2B_hit_output')
hit_file4 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX3X_hit_output')
hit_file5 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX3Y_hit_output')
hit_file6 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX4_hit_output')
hit_file7 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX5_hit_output')
hit_file8 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX6_hit_output')
hit_file9 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX10_hit_output')
hit_file10 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX17_hit_output')
hit_file11 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX18_hit_output')
hit_file12 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX19A_hit_output')
hit_file13 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX19B_hit_output')
hit_file14 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX20_hit_output')
hit_file15 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX21_hit_output')
hit_file16 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX23_hit_output')
hit_file17 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX24_hit_output')
hit_file18 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX25_hit_output')
hit_file19 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX27_hit_output')
hit_file20 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX28_hit_output')
hit_file21 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX31_hit_output')
hit_file22 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX39A_hit_output')
hit_file23 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX39B_hit_output')
hit_file24 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX41_hit_output')
hit_file25 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX42_hit_output')
hit_file26 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX43_hit_output')
hit_file27 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX46_hit_output')
hit_file28 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX47_hit_output')
hit_file29 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX48_hit_output')
hit_file30 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX49_hit_output')
hit_file31 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX50_hit_output')
hit_file32 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX51_hit_output')
hit_file33 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX52_hit_output')
hit_file34 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX53_hit_output')
hit_file35 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX54_hit_output')
hit_file36 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX55_hit_output')
hit_file37 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX56_hit_output')
hit_file38 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hit/DDX59_hit_output')

hit_data1 = csv.reader(hit_file1, delimiter='\t')
hit_data2 = csv.reader(hit_file2, delimiter='\t')
hit_data3 = csv.reader(hit_file3, delimiter='\t')
hit_data4 = csv.reader(hit_file4, delimiter='\t')
hit_data5 = csv.reader(hit_file5, delimiter='\t')
hit_data6 = csv.reader(hit_file6, delimiter='\t')
hit_data7 = csv.reader(hit_file7, delimiter='\t')
hit_data8 = csv.reader(hit_file8, delimiter='\t')
hit_data9 = csv.reader(hit_file9, delimiter='\t')
hit_data10 = csv.reader(hit_file10, delimiter='\t')
hit_data11 = csv.reader(hit_file11, delimiter='\t')
hit_data12 = csv.reader(hit_file12, delimiter='\t')
hit_data13 = csv.reader(hit_file13, delimiter='\t')
hit_data14 = csv.reader(hit_file14, delimiter='\t')
hit_data15 = csv.reader(hit_file15, delimiter='\t')
hit_data16 = csv.reader(hit_file16, delimiter='\t')
hit_data17 = csv.reader(hit_file17, delimiter='\t')
hit_data18 = csv.reader(hit_file18, delimiter='\t')
hit_data19 = csv.reader(hit_file19, delimiter='\t')
hit_data20 = csv.reader(hit_file20, delimiter='\t')
hit_data21 = csv.reader(hit_file21, delimiter='\t')
hit_data22 = csv.reader(hit_file22, delimiter='\t')
hit_data23 = csv.reader(hit_file23, delimiter='\t')
hit_data24 = csv.reader(hit_file24, delimiter='\t')
hit_data25 = csv.reader(hit_file25, delimiter='\t')
hit_data26 = csv.reader(hit_file26, delimiter='\t')
hit_data27 = csv.reader(hit_file27, delimiter='\t')
hit_data28 = csv.reader(hit_file28, delimiter='\t')
hit_data29 = csv.reader(hit_file29, delimiter='\t')
hit_data30 = csv.reader(hit_file30, delimiter='\t')
hit_data31 = csv.reader(hit_file31, delimiter='\t')
hit_data32 = csv.reader(hit_file32, delimiter='\t')
hit_data33 = csv.reader(hit_file33, delimiter='\t')
hit_data34 = csv.reader(hit_file34, delimiter='\t')
hit_data35 = csv.reader(hit_file35, delimiter='\t')
hit_data36 = csv.reader(hit_file36, delimiter='\t')
hit_data37 = csv.reader(hit_file37, delimiter='\t')
hit_data38 = csv.reader(hit_file38, delimiter='\t')
# # ---------------------------------------------------------------------------------------------------------------------------
#
# #read through the file1 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hit_data1:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX1','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file2 and insert each row into the table
firstline = True
for row in hit_data2:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX2A','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file3 and insert each row into the table
firstline = True
for row in hit_data3:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX2B','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file4 and insert each row into the table
firstline = True
for row in hit_data4:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX3X','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file5 and insert each row into the table
firstline = True
for row in hit_data5:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX3Y','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file6 and insert each row into the table
firstline = True
for row in hit_data6:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX4','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file7 and insert each row into the table
firstline = True
for row in hit_data7:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX5','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file8 and insert each row into the table
firstline = True
for row in hit_data8:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX6','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file9 and insert each row into the table
firstline = True
for row in hit_data9:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX10','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file10 and insert each row into the table
firstline = True
for row in hit_data10:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX17','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file11 and insert each row into the table
firstline = True
for row in hit_data11:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX18','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file12 and insert each row into the table
firstline = True
for row in hit_data12:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX19A','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file13 and insert each row into the table
firstline = True
for row in hit_data13:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX19B','Query_1',%s,%s,%s,%s)", row)
conn.commit()

# #read through the file14 and insert each row into the table
firstline = True
for row in hit_data14:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX20','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file15 and insert each row into the table
firstline = True
for row in hit_data15:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX21','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file16 and insert each row into the table
firstline = True
for row in hit_data16:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX23','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file17 and insert each row into the table
firstline = True
for row in hit_data17:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX24','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file18 and insert each row into the table
firstline = True
for row in hit_data18:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX25','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file19 and insert each row into the table
firstline = True
for row in hit_data19:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX27','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file20 and insert each row into the table
firstline = True
for row in hit_data20:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX28','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file21 and insert each row into the table
firstline = True
for row in hit_data21:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX31','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file22 and insert each row into the table
firstline = True
for row in hit_data22:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX39A','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file23 and insert each row into the table
firstline = True
for row in hit_data23:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX39B','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file24 and insert each row into the table
firstline = True
for row in hit_data24:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX41','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file25 and insert each row into the table
firstline = True
for row in hit_data25:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX42','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file26 and insert each row into the table
firstline = True
for row in hit_data26:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX43','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file27 and insert each row into the table
firstline = True
for row in hit_data27:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX46','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file28 and insert each row into the table
firstline = True
for row in hit_data28:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX47','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file29 and insert each row into the table
firstline = True
for row in hit_data29:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX48','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file30 and insert each row into the table
firstline = True
for row in hit_data30:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX49','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file31 and insert each row into the table
firstline = True
for row in hit_data31:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX50','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file32 and insert each row into the table
firstline = True
for row in hit_data32:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX51','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file33 and insert each row into the table
firstline = True
for row in hit_data33:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX52','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file34 and insert each row into the table
firstline = True
for row in hit_data34:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX53','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file35 and insert each row into the table
firstline = True
for row in hit_data35:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX54','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file36 and insert each row into the table
firstline = True
for row in hit_data36:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX55','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file37 and insert each row into the table
firstline = True
for row in hit_data37:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX56','Query_1',%s,%s,%s,%s)", row)
conn.commit()
#
# # read through the file38 and insert each row into the table
firstline = True
for row in hit_data38:
     if firstline:    #skip first line
           firstline = False
           continue
     cursor.execute("INSERT INTO blast_hit (Gene_Symbol, query_id, hit_num, hit_id, hit_accession, hit_len) VALUES ('DDX59','Query_1',%s,%s,%s,%s)", row)
conn.commit()


# -----create table6------------------------------------------------------------------
cursor.execute("CREATE TABLE IF NOT EXISTS blast_hsp (Gene_Symbol varchar(45), hsp_num MEDIUMTEXT, hsp_bit_score MEDIUMTEXT, hsp_evalue MEDIUMTEXT, hsp_query_from MEDIUMTEXT, "
               "hsp_query_to MEDIUMTEXT, hsp_identity MEDIUMTEXT, hsp_positive MEDIUMTEXT, hsp_align_len MEDIUMTEXT, hsp_qseq TEXT, hsp_hseq TEXT)")
conn.commit()

hsp_file1 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX1_hsp_output')
hsp_file2 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX2A_hsp_output')
hsp_file3 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX2B_hsp_output')
hsp_file4 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX3X_hsp_output')
hsp_file5 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX3Y_hsp_output')
hsp_file6 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX4_hsp_output')
hsp_file7 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX5_hsp_output')
hsp_file8 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX6_hsp_output')
hsp_file9 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX10_hsp_output')
hsp_file10 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX17_hsp_output')
hsp_file11 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX18_hsp_output')
hsp_file12 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX19A_hsp_output')
hsp_file13 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX19B_hsp_output')
hsp_file14 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX20_hsp_output')
hsp_file15 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX21_hsp_output')
hsp_file16 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX23_hsp_output')
hsp_file17 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX24_hsp_output')
hsp_file18 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX25_hsp_output')
hsp_file19 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX27_hsp_output')
hsp_file20 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX28_hsp_output')
hsp_file21 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX31_hsp_output')
hsp_file22 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX39A_hsp_output')
hsp_file23 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX39B_hsp_output')
hsp_file24 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX41_hsp_output')
hsp_file25 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX42_hsp_output')
hsp_file26 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX43_hsp_output')
hsp_file27 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX46_hsp_output')
hsp_file28 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX47_hsp_output')
hsp_file29 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX48_hsp_output')
hsp_file30 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX49_hsp_output')
hsp_file31 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX50_hsp_output')
hsp_file32 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX51_hsp_output')
hsp_file33 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX52_hsp_output')
hsp_file34 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX53_hsp_output')
hsp_file35 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX54_hsp_output')
hsp_file36 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX55_hsp_output')
hsp_file37 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX56_hsp_output')
hsp_file38 = open('C:/Users/Sasan Najar/Desktop/internalBLAST-xml/hsp/DDX59_hsp_output')

hsp_data1 = csv.reader(hsp_file1, delimiter='\t')
hsp_data2 = csv.reader(hsp_file2, delimiter='\t')
hsp_data3 = csv.reader(hsp_file3, delimiter='\t')
hsp_data4 = csv.reader(hsp_file4, delimiter='\t')
hsp_data5 = csv.reader(hsp_file5, delimiter='\t')
hsp_data6 = csv.reader(hsp_file6, delimiter='\t')
hsp_data7 = csv.reader(hsp_file7, delimiter='\t')
hsp_data8 = csv.reader(hsp_file8, delimiter='\t')
hsp_data9 = csv.reader(hsp_file9, delimiter='\t')
hsp_data10 = csv.reader(hsp_file10, delimiter='\t')
hsp_data11 = csv.reader(hsp_file11, delimiter='\t')
hsp_data12 = csv.reader(hsp_file12, delimiter='\t')
hsp_data13 = csv.reader(hsp_file13, delimiter='\t')
hsp_data14 = csv.reader(hsp_file14, delimiter='\t')
hsp_data15 = csv.reader(hsp_file15, delimiter='\t')
hsp_data16 = csv.reader(hsp_file16, delimiter='\t')
hsp_data17 = csv.reader(hsp_file17, delimiter='\t')
hsp_data18 = csv.reader(hsp_file18, delimiter='\t')
hsp_data19 = csv.reader(hsp_file19, delimiter='\t')
hsp_data20 = csv.reader(hsp_file20, delimiter='\t')
hsp_data21 = csv.reader(hsp_file21, delimiter='\t')
hsp_data22 = csv.reader(hsp_file22, delimiter='\t')
hsp_data23 = csv.reader(hsp_file23, delimiter='\t')
hsp_data24 = csv.reader(hsp_file24, delimiter='\t')
hsp_data25 = csv.reader(hsp_file25, delimiter='\t')
hsp_data26 = csv.reader(hsp_file26, delimiter='\t')
hsp_data27 = csv.reader(hsp_file27, delimiter='\t')
hsp_data28 = csv.reader(hsp_file28, delimiter='\t')
hsp_data29 = csv.reader(hsp_file29, delimiter='\t')
hsp_data30 = csv.reader(hsp_file30, delimiter='\t')
hsp_data31 = csv.reader(hsp_file31, delimiter='\t')
hsp_data32 = csv.reader(hsp_file32, delimiter='\t')
hsp_data33 = csv.reader(hsp_file33, delimiter='\t')
hsp_data34 = csv.reader(hsp_file34, delimiter='\t')
hsp_data35 = csv.reader(hsp_file35, delimiter='\t')
hsp_data36 = csv.reader(hsp_file36, delimiter='\t')
hsp_data37 = csv.reader(hsp_file37, delimiter='\t')
hsp_data38 = csv.reader(hsp_file38, delimiter='\t')
#
# #read through the file1 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data1:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX1',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file2 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data2:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX2A',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file3 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data3:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX2B',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file4 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data4:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX3X',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file5 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data5:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX3Y',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file6 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data6:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX4',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file7 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data7:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX5',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file8 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data8:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX6',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file9 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data9:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX10',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file10 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data10:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX17',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file11 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data11:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX18',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file12 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data12:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX19A',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file13 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data13:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX19B',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file14 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data14:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX20',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file15 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data15:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX21',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file16 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data16:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX23',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file17 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data17:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX24',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
#
# #read through the file18 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data18:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX25',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file19 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data19:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX27',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file20 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data20:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX28',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file21 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data21:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX31',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
#
# #read through the file22 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data22:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX39A',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file23 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data23:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX39B',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file24 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data24:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX41',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file25 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data25:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX42',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file26 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data26:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX43',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file27 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data27:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX46',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file28 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data28:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX47',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file29 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data29:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX48',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file30 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data30:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX49',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file31 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data31:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX50',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file32 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data32:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX51',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()

# #read through the file33 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data33:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX52',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file34 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data34:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX53',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()

# #read through the file35 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data35:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX54',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()

# #read through the file36 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data36:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX55',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file37 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data37:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX56',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()
#
# #read through the file38 and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in hsp_data38:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO blast_hsp (Gene_Symbol, hsp_num, hsp_bit_score, hsp_evalue, hsp_query_from, hsp_query_to, "
                 "hsp_identity, hsp_positive, hsp_align_len, hsp_qseq, hsp_hseq) VALUES ('DDX59',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
conn.commit()


# -----create table7
cursor.execute("CREATE TABLE alignment (alignment_id varchar(45), Gene_Symbol varchar(45), seq_header MEDIUMTEXT, seq_len MEDIUMTEXT, sequence MEDIUMTEXT)")
conn.commit()
#
align_fasta_file = open('C:/Users/Sasan Najar/PycharmProjects/untitled/fasta_output')
#
align_fasta_data = csv.reader(align_fasta_file, delimiter='\t')
#
# #read through the file and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in align_fasta_data:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO alignment (alignment_id, Gene_Symbol, seq_header, seq_len, sequence) VALUES (%s,%s,%s,%s,%s)", row)
conn.commit()

#-----create table8
cursor.execute("CREATE TABLE scoringPoint (matched INTEGER , mismatched INTEGER , gap INTEGER)")
conn.commit()
cursor.execute("INSERT INTO scoringPoint (matched, mismatched, gap) VALUES ('1','0','-2')")
conn.commit()


#-----create table9 changed to alignment_big
cursor.execute("CREATE TABLE alignemntSolution (alignment_id MEDIUMTEXT, alignmentSol_ref MEDIUMTEXT, c1 MEDIUMTEXT, C2 MEDIUMTEXT )")
conn.commit()

#-----create table10
cursor.execute("CREATE TABLE conservedPosition (entry_id varchar(45), file_name mediumtext, seq_id mediumtext, DEAD_BOX_start_pos int, DEAD_BOX_end_pos int)")
conn.commit()
motif_inputfile = open('C:/Users/Sasan Najar/PycharmProjects/untitled/DEADBOX_output')

motif_data = csv.reader(motif_inputfile, delimiter='\t')
for row in motif_data:
   print row

# #read through the motif_data and insert each row into the table--------------------------------------------------------------------
firstline = True
for row in motif_data:
  if firstline:    #skip first line
      firstline = False
      continue
  cursor.execute("INSERT INTO conservedPosition (entry_id, file_name, seq_id, DEAD_BOX_start_pos, DEAD_BOX_end_pos) VALUES (%s,%s,%s,%s,%s)", row)
conn.commit()

#--------- create table alignment_big
str1 = "CREATE TABLE alignment_big (entry_id INTEGER, pos_0 char)"
cursor.execute(str1)
conn.commit()

str3 = "ALTER TABLE alignment_big ADD COLUMN ("
str2 = "pos_"

for i in xrange(1,940):
  str4 = str3 + str2+str(i)+ " char)"
  print str4
  cursor.execute(str4)
  conn.commit()
