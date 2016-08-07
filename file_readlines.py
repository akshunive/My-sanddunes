#to read and print
fp=open('files.txt','r')
while(1):
	data=fp.readline()  #here data will act as list to store multiple lines as input
	print data
	if not data:         
		break
for line in data:
	print line

fp.seek(0,0)   #to move the filepointer again to starting of the file
data=fp.read()
print data