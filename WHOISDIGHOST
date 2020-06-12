#!/usr/bin/python3
import os
def domainName():
	i=input("Domain name: "); return i
def fileName():
	i=input("File name: "); return i
def toFile(filename):
	try:
		file = open("%s"%(filename),"r+")
	except FileNotFoundError:
		print("Ah no file with this name exists, would you like to make one?('y' to continue, or anything else exits).\n"); nf=input("$: ")
		try:
			if nf == "y":
				os.system("touch %s"%(filename))
			else:
				print("Oh no worries then, Later!\n"); exit()
		except IOError:
			print("Oh dear, the input was not as expected, please try again!\n"); exit()
def StartDig(d_name,f_name):
	print("Getting whois infomation...\n"); os.system("whois %s >> %s"%(d_name,f_name))
	print("Getting dig infomation...\n"); os.system("dig %s >> %s"%(d_name,f_name))
	print("Getting host infomation...\n"); os.system("host %s >> %s"%(d_name,f_name))
	print("The file is made.")
def GetIP(domain):
	os.system("touch tmp.txt && ping -c 1 %s > tmp.txt"%(domain)); file = open("tmp.txt","r+")
	for x in file.readlines(1):
		y = x
	y = y.split(); y = y[2]; y = y.split("("); y = y[1]; y = y.split(")"); y = y[0]; file.close(); os.system("rm tmp.txt")
	print("\nThe public IP from a ping is: %s\n:Note: this could be a load ballencer or a WAF, not the actual target IP!\n"%(y))
def main():
	try:
		print("\t\t\t\tWHOISDIGHOST.py\nThese are the files in this directory (for reference). Be careful to not overwrite files!\n"); os.system("ls -alt")
		dname=domainName(); fname=fileName(); toFile("%s"%(fname)); GetIP(dname); StartDig(dname,fname)
	except KeyboardInterrupt:
		print("\nKeyboard Interupt! Exiting!\n")
	except IOError:
		print("Input/output error.")
if __name__ == "__main__":
	main()
