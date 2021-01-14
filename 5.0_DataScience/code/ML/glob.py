import glob
for filename in glob.iglob('/home/hadoop/J2EE_TRAINING/Python/code/*.py', recursive=True):
   print(filename)
