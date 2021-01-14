import sys

try:
   # open file stream
   #file = open('/home/hadoop/J2EE_TRAINING/Python/test.txt', 'r')

open('/home/hadoop/J2EE_TRAINING/Python/test.txt').read()
open('/home/hadoop/J2EE_TRAINING/Python/test.txt').readlines()


file = open('/home/hadoop/J2EE_TRAINING/Python/test.txt', 'w')
file.write('a\nb\nc')
file.close()

except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()
  
