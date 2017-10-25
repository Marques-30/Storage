import webbrowser
import os
import svn
import sys
import subprocess

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
	message = "File was added by script"
g = subprocess.Popen(["svn", "commit", "https://subversion/repos/BIDM/"+File_source+"/"+source+"/"+target, "--message", message], stdout=subprocess.PIPE)
print g.communicate()
end=raw_input("New tag is created")