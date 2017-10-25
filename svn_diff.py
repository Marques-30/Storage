import webbrowser
import os
import svn
import sys
import subprocess

choice = raw_input("Would you like this program to run automatically or manual control: \n")

def auto():
	Document = raw_input("Enter the name of the CSV document: ")
	Object = open(Document+".csv", "r")
	cut=str(Object.read()).split(",")
	File_source = cut[0]
	source = cut[1]
	target = cut[2] #raw_input("Enter the name new branch folder you would like to create:\n")
	g = subprocess.Popen(["svn", "diff", "--summarize", "--xml", "https://subversion/repos/BIDM/"+File_source+"/"+source, "https://subversion/repos/BIDM/"+File_source+"/"+target], stdout=subprocess.PIPE)
	end=raw_input("")

def manual():
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	print p.communicate()
	File_source = raw_input("Enter the name of the environment: ")
	h = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+File_source.upper()], stdout=subprocess.PIPE)
	print h.communicate()
	source = raw_input("Enter the name of the original folder: ")
	#file = raw_input("Enter the name of the file: ")
	target = raw_input("Enter the name of the target folder: ")
	g = subprocess.Popen(["svn", "diff", "--summarize", "--xml", "https://subversion/repos/BIDM/"+File_source+"/"+source, "https://subversion/repos/BIDM/"+File_source+"/"+target], stdout=subprocess.PIPE)
	print g.communicate()
	end=raw_input("")
#stdout, stderr = p.communicate()
#reader = csv.DictReader(stdout.decode('ascii').splitlines(),
                    #delimiter=' ', skipinitialspace=True,
                    #fieldnames=[''])

#for rows in reader:
#	writer.writerow(rows)
if __name__ == '__main__':
	if choice.lower() == "manual":
		manual()
	else:
		auto()