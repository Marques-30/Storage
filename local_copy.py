import webbrowser
import os	
from shutil import copy
from shutil import copytree
import shutil
import svn
import fileinput, sys
import subprocess

LanID = raw_input("Please enter Lan-ID: ")
File_path = raw_input("Enter the name of the folder the file is in?\n")
FC = raw_input("Which file would you like to copy?\n")
path = raw_input("Enter the name of the folder you are moving to?\n")
shutil.copy("C:\Users\\"+LanID+"\documents\\" + File_path + "\\"+ FC, "C:\Users\\"+LanID+"\Desktop\\"+path)
print "File copy complete"