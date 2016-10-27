import os
from os import listdir
from os.path import isfile, join

dict = {"":""}
def all_files(key_word):
	for path, dirs, files in os.walk('\\'):
		for p in path:
			p2 = p.lower()
			if(p not in dict):
				dict[p2] = [p]
			else:
				dict[p2].append(p)
		for directory in dirs:
			dir2 = directory.lower()
			if(directory not in dict):
				dict[dir2] = [os.path.join(path,directory)]
			else:
				dict[dir2].append(os.path.join(path,directory))
		for name in files:
			n2 = name.lower()
			if(name not in dict):
				dict[n2] = [os.path.join(path,name)]
			else:
				dict[n2].append(os.path.join(path,name))

print "Please wait while keywords and paths are stored into a dictionary!"
all_files('.txt')
print "Loaded\n"

while(1):
	print "----------------------------------------------------------------------------"
	key = raw_input("Enter key word to search: ")
	print "\n"
	key = key.lower()
	check = 0
	for a in dict:
		if(a.find(key) > 0):
			lst = dict[a]
			for p in lst:
				print p