import webbrowser
import os	
import svn
import fileinput, sys
import subprocess

LanID = raw_input("Please enter Lan-ID: ")
CF = raw_input("What name would you like to give the folder you are creating: ")
choice = raw_input("Would you like this program to run automatically or manual control: \n")

def auto():
	Document = raw_input("Enter the name of the CSV document: ")
	Object = open(Document+".csv", "r")
	cut=str(Object.read()).split(",")
	File_source = cut[0]
	source = cut[1]
	p = subprocess.Popen(["svn", "export", "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file+"/", "C:\\Users\\"+LanID+"\\Desktop\\"+CF], stdout=subprocess.PIPE)

def manual():
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"], stdout=subprocess.PIPE)
	print p.communicate()
	copy_envir = raw_input("Where you are directing the folder.\nEnter the name of the environment: ")
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+copy_envir], stdout=subprocess.PIPE)
	print p.communicate()
	copy_file = raw_input("Enter the name of the folder you are updating: ")
	p = subprocess.Popen(["svn", "export", "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file+"/", "C:\\Users\\"+LanID+"\\Desktop\\"+CF], stdout=subprocess.PIPE)
	print p.communicate()

if __name__ == '__main__':
	if choice.lower() == "manual":
		manual()
	else:
		auto()
print "file copied"