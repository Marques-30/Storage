import webbrowser
import os
import svn
import sys
import csv
import subprocess

choice = raw_input("Would you like this program to run automatically or manual control: \n")

def manual():
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	print p.communicate()
	File_source = raw_input("Enter the name of the environment folder:\n")
	h = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+File_source.upper()], stdout=subprocess.PIPE)
	print h.communicate()
	source = raw_input("Enter the name of the folder you want to access:\n")
	target = raw_input("Enter the name new branch folder you would like to create:\n")
	prompt = raw_input("Would you like to place a comment on this: ")
	if prompt.lower() == "yes":
		message = raw_input("What is your comment for this file:\n")
	else:
		message = " "
	g = subprocess.Popen(["svn", "mkdir", "https://subversion/repos/BIDM/"+File_source+"/"+source+"/"+target, "--message", message], stdout=subprocess.PIPE)
	p = subprocess.Popen(["svn", "log", "--verbose", "--xml", "https://subversion/repos/BIDM/"+File_source+"/"+source], stdout=subprocess.PIPE)

def auto():
	Document = raw_input("Enter the name of the CSV document: ")
	Object = open(Document+".csv", "r")
	cut=str(Object.read()).split(",")
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	File_source = cut[0]
	h = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+File_source.upper()], stdout=subprocess.PIPE)
	source = cut[1]
	target = raw_input("Enter the name new branch folder you would like to create:\n")
	prompt = raw_input("Would you like to place a comment on this: ")
	if prompt.lower() == "yes":
		message = raw_input("What is your comment for this file:\n")
	else:
		message = cut[2]
	g = subprocess.Popen(["svn", "mkdir", "https://subversion/repos/BIDM/"+File_source+"/"+source+"/"+target, "--message", message], stdout=subprocess.PIPE)
	p = subprocess.Popen(["svn", "log", "--verbose", "--xml", "https://subversion/repos/BIDM/"+File_source+"/"+source], stdout=subprocess.PIPE)

if __name__ == '__main__':
	if choice.lower() == "manual":
		manual()
	else:
		auto()

command = p.communicate()
end=raw_input("New branch is created")
data = open("file.csv", "w")
writer = csv.writer(file, lineterminator='\n')
writer.writerow(command)