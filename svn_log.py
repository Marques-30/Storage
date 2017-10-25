import webbrowser
import os
import re
import csv
import itertools
import svn
import fileinput, sys
import subprocess

command = raw_input("Would you like this program to run automatically or manual control: \n")

def Compare():
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM"], stdout=subprocess.PIPE)
	print p.communicate()
	File_path = raw_input("\nEnter the name of the environment: ")
	p = subprocess.Popen(["svn", "list","https://subversion/repos/BIDM/"+File_path], stdout=subprocess.PIPE)
	print p.communicate()
	folder = raw_input("\nEnter the name of the folder: ")
	p = subprocess.Popen(["svn", "log", "-v", "--xml", "https://subversion/repos/BIDM/"+File_path+"/"+folder], stdout=subprocess.PIPE)
	print p.communicate()

def Detail():
	Document = raw_input("Enter the name of the CSV document: ")
	Object = open(Document+".csv", "r")
	cut=str(Object.read()).split(",")
	File_source = cut[0]
	source = cut[1]
	target = raw_input("Enter the name new branch folder you would like to create:\n")
	p = subprocess.Popen(["svn", "log", "--verbose", "--xml", "https://subversion/repos/BIDM/"+File_source+"/"+source+"/"+target, "C:\Users\Butilm01\Documents\SVN\SVN Python Scripts\Test.xml"], stdout=subprocess.PIPE)
	#print "\nsvn", "log", "--verbose", "https://subversion/repos/BIDM/"+File_path+"/"+folder+"\n"
	print p.communicate()

if __name__ == '__main__':
	if command.lower() == "manual":
		Compare()
	else:
		Detail()
