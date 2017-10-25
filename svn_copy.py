import webbrowser
import os
import re
from shutil import copy
from shutil import copytree
import shutil
import svn
import fileinput, sys
import subprocess

choice = raw_input("Would you like this program to run automatically or manual control: \n")

def auto():
	Document = raw_input("Enter the name of the CSV document: ")
	Object = open(Document+".csv", "r")
	cut=str(Object.read()).split(",")
	File_path = cut[0]
	path = cut[1]
	copy_envir = cut[2]
	copy_file = cut[3]
	prompt = raw_input("Would you like to place a comment on this: ")
	if prompt.lower() == "yes":
		message = raw_input("What is your comment for this file:\n")
	else:
		message = " "
	p = subprocess.Popen(["svn", "copy", "https://subversion/repos/BIDM/"+File_path+"/"+path+"/", "--message", message, "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file+"/"], stdout=subprocess.PIPE)
	print p.communicate()
	print "The folder has been copied"
	p = subprocess.Popen(["svn", "diff", "--summarize", "--xml", "https://subversion/repos/BIDM/"+File_path+"/"+path, "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file], stdout=subprocess.PIPE)
	print p.communicate()

def manual():
	#original
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	print p.communicate()
	File_path = raw_input("For the original folder.\nEnter the name of the environment: ")
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+File_path], stdout=subprocess.PIPE)
	print p.communicate()
	path = raw_input("Enter the name of the folder: ")
	#target
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	print p.communicate()
	copy_envir = raw_input("For where you are directing the folder.\nEnter the name of the environment: ")
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+copy_envir], stdout=subprocess.PIPE)
	print p.communicate()
	copy_file = raw_input("Enter the name of the folder: ")
	prompt = raw_input("Would you like to place a comment on this: ")
	if prompt.lower() == "yes":
		message = raw_input("What is your comment for this file:\n")
	else:
		message = " "
	p = subprocess.Popen(["svn", "copy", "https://subversion/repos/BIDM/"+File_path+"/"+path+"/", "--message", message, "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file+"/"], stdout=subprocess.PIPE)
	print p.communicate()
	print "The folder has been copied"
	p = subprocess.Popen(["svn", "diff", "--summarize", "--xml", "https://subversion/repos/BIDM/"+File_path+"/"+path, "https://subversion/repos/BIDM/"+copy_envir+"/"+copy_file], stdout=subprocess.PIPE)
	print p.communicate()

if __name__ == '__main__':
	if choice.lower() == "manual":
		manual()
	else:
		auto()

end=raw_input("Program has finished")