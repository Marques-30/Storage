import webbrowser
import os	
from shutil import copy
from shutil import copytree
import shutil
import svn
import fileinput, sys
import subprocess

LanID = raw_input("Please enter Lan-ID: ")
source = raw_input("What is the original folder you want to compare to? ")
target = raw_input("What is the target folder you want to compare to? ")
src = os.listdir('C:\Users\\'+LanID+'\Desktop\\' + source)
tar = os.listdir('C:\Users\\'+LanID+'\Desktop\\' + target)
src_files = len(src)
tar_files = len(tar)
#for line in fileinput.input("C:\\Users\\"+LanID+"\\Desktop\\" + source):
#	line = line[0:-1]
#	sc = ''.join((line,'.txt'))
#	tr = ''.join((line,'.txt'))
#	for root, dirs, files in os.walk(r"C:\\Users\\"+LanID+"\\Desktop\\" + target):
#		if sc in files:
#			pytime = os.path.getmtime(os.path.join(root, sc))
#			print(sc, '   :', pytime)
#			for root, dirs, files in os.walk(root):
#				if txt in files:
#					txttime = os.path.getmtime(os.path.join(root, txt))
#					print(txt, '  :', txttime)
print "\nThere are " + str(src_files) + " Files within " + source + " Folder."
print "\nThere are " + str(tar_files) + " Files within " + target + " Folder."