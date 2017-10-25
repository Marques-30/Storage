import webbrowser
import os	
import svn
import fileinput, sys
import subprocess

LanID = raw_input("Please enter Lan-ID: ")
CF = raw_input("Which folder would you like to copy? ")
choice = raw_input("Would you like this program to run automatically or manual control: \n")

def manual():
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"], stdout=subprocess.PIPE)
	print p.communicate()
	copy_envir = raw_input("Where you are directing the folder.\nEnter the name of the environment: ")
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+copy_envir], stdout=subprocess.PIPE)
	print p.communicate()
	copy_file = raw_input("Enter the name of the folder: ")
	prompt = raw_input("Would you like to place a comment on this: ")
	if prompt.lower() == "yes":
		message = raw_input("What is your comment for this file:\n")
	else:
		message = ""
	p = subprocess.Popen(["svn", "import", "C:\Users\\"+LanID+"\Desktop\\"+CF, "--message", message, "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file+"/"], stdout=subprocess.PIPE)

def auto():
	Document = raw_input("Enter the name of the CSV document: ")
	Object = open(Document + ".csv", "r")
	cut=str(Object.read()).split(",")
	copy_envir = cut[0]
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+copy_envir], stdout=subprocess.PIPE)
	copy_file = cut[1]
	prompt = raw_input("Would you like to place a comment on this: ")
	if prompt.lower() == "yes":
		message = raw_input("What is your comment for this file:\n")
	else:
		message = ""
	p = subprocess.Popen(["svn", "import", "C:\Users\\"+LanID+"\Desktop\\"+CF, "--message", message, "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file+"/"], stdout=subprocess.PIPE)

if __name__ == '__main__':
	if choice.lower() == "manual":
		manual()
	else:
		auto()

print "file copied"