'''5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''


class Sample:
	def __init__(self):       #constructor 
		print "constructor is being executed"
	def getString(self):      #function to get input
		self.string=raw_input("Enter the string:")
	def printString(self):    #function to print the input
		print self.string.upper()

s=Sample()                    #s is an object created for class sample
s.getString()
s.printString()
		
