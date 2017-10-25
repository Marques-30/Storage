import webbrowser
import os	
from shutil import copy
from shutil import copytree
import shutil
import svn
import fileinput, sys
import subprocess

LanID = raw_input("Please enter Lan-ID: ")
CF = raw_input("Which folder would you like to copy? ")
link = raw_input("Enter the name of the folder you are creating? ")
Folder_dst = 'C:\Users\\'+LanID+'\Desktop\\' + link
shutil.copytree("C:\Users\\"+LanID+"\Documents\\" + CF, "C:\Users\\"+LanID+"\Desktop\\"+link)
print "The folder has been copied"