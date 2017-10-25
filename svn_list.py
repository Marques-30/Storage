import webbrowser
import os
import re
import csv
import itertools
import svn
import fileinput, sys
import subprocess


with open("list.csv", 'w') as out_file:
	writer=csv.writer(out_file, delimiter=",", lineterminator='\n')
	header = ['Revision', 'Updated By', 'Month', 'Year', 'Time', 'Environment']
	
	lead = ['BIDM']
	o = subprocess.Popen(["svn", "list", "https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	print o.communicate()
	p = subprocess.Popen(["svn", "list", "--verbose", "https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	stdout, stderr = p.communicate()
	reader = csv.DictReader(stdout.decode('ascii').splitlines(),
	                    delimiter=' ', skipinitialspace=True,
	                    fieldnames=['Revision', 'Updated By', 'Month', 'Year', 'Time', 'Environment'])

	#writer.writerow((lead))
	#writer.writerow((header))
	#for rows in reader:
	#	writer.writerow(rows)

	#############################################################################

	File_path = raw_input("Enter the name of the environment: ")
	middle = [File_path]
	d = subprocess.Popen(["svn", "list", "--verbose", "https://subversion/repos/BIDM/"+File_path], stdout=subprocess.PIPE)
	stdout, stderr = d.communicate()
	k = subprocess.Popen(["svn", "list", "https://subversion/repos/BIDM/"+File_path], stdout=subprocess.PIPE)
	print k.communicate()
	reader = csv.DictReader(stdout.decode('ascii').splitlines(),
	                    delimiter=' ', skipinitialspace=True,
	                    fieldnames=['Revision', 'Updated By', 'Month', 'Year', 'Time', 'Environment'])

	for rows in reader:
		print(rows)
		line2 = rows
	print line2

	#########################################################################

	path = raw_input("Enter the name of the folder: ")
	end = [path]
	l = subprocess.Popen(["svn", "list", "--verbose", "https://subversion/repos/BIDM/"+File_path+"/"+path], stdout=subprocess.PIPE)
	stdout, stderr = l.communicate()
	r = subprocess.Popen(["svn", "list", "https://subversion/repos/BIDM/"+File_path+"/"+path], stdout=subprocess.PIPE)
	print r.communicate()
	reader = csv.DictReader(stdout.decode('ascii').splitlines(),
	                    delimiter=' ', skipinitialspace=True,
	                    fieldnames=['Revision', 'Updated By', 'Month', 'Year', 'Time', 'Environment'])

	for rows in reader:
		print(rows)
		line3 = rows
	print line3
	f = raw_input("Program End")

	###########################################################################

	#writer.writerow((middle))
	#writer.writerow((header))
	#writer.writerow(line2)
	#writer.writerow((end))
	#writer.writerow((header))
	#writer.writerow(line3)