#to print the factorial of all numbers within the given number
lst=[]
def facto():                        #function definition
	try:
		num=input("enter a number:")
		f=1
		for i in range(1,num+1):    #checking the number within limit
			f=f*i                   #factorial formula
			lst.append(f) 
		print lst
	except Exception:
		print "....error occured...."

facto()  #function call