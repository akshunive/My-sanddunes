#opening a file and writing into it and creating log files 
import logging
logging.basicConfig(filename="files.log",level=logging.DEBUG)
fp=open('files.txt','a')
logging.info("file opened in append mode")
fp.write("His name is rufus.")
fp.close()
fp=open('files.txt','r')
logging.info("file opened in read mode")
data=fp.read()
print data
logging.info("end of file")
