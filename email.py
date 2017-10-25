import win32com.client
from win32com.client import Dispatch, constants

const=win32com.client.constants
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
First_Name = raw_input("First Name: ")
Last_Name = raw_input("Last Name: ")
newMail.Subject = raw_input("Subject: ")
newMail.Body = "Testing of email notification"
newMail.BodyFormat = 2 # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
#newMail.HTMLBody = "<HTML><BODY>Enter the <span style='color:red'>message</span> text here.</BODY></HTML>"
newMail.To = First_Name+"."+Last_Name+"@bankofthewest.com; " + "marques.butilla@bankofthewest.com;"
choice = raw_input("Would you like to add attachment? Y/N: ")
if choice.lower() == "y":
	LANID = raw_input("Please enter your Lan ID: ")
	file = raw_input("What is the file or folder name: ")
	attachment1 = r"C:\\Users\\"+LANID+"\\Desktop\\"+file
	newMail.Attachments.Add(Source=attachment1)
	newMail.display()
	newMail.send
else:
	newMail.display()
	newMail.send