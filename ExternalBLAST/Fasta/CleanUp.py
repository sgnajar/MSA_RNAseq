import re
import sys
import os

# count = 0
file = raw_input("File to clean-up: ")

#print "Name of file: " , file

# for doc in os.listdir('/Users/snajar/Desktop/DatabaseProject/ExternalBLAST/Fasta'):
# 	doc1 = "doc_path" + doc
# 	doc2 = "/Users/snajar/Desktop/DatabaseProject/ExternalBLAST/CleanedFasta" + doc1

f = open(file,'r')
f2 = open(file+"cleaned",'w')
#for line in f.read().split('\n'):
for line in f:
# 	if line.startswith(">"):
 		line = re.sub ('-' ,' ', line)
 		line = re.sub ('\|' ,' ' , line)
 		f2.write(line)

f.close()
f2.close()

# if __name__ == "__main__":
# 	print "argument: ", sys.argv
# 	
# 	inputfile = sys.argv[1]
# 	print "Input:", inputfile
# 
# 	outputfile = inputfile 
# 	print "Output:", outputfile
#  f = open(inputfile,'r')
# 	for line in inputfile.read().split('\n'):
# 		print line
# for line in f:
# 	if line.startswith(">"):
# 		line = re.sub ('-' ,' ', line)
# 		line = re.sub ('\|' ,' ' , line)
# 		f2.write(line)	
	