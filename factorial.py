lst=[]
def facto():  #function definition
	try:
		num=input("enter a numbers:")
        factorial=1
		for i in range(1,num+1):
			factorial=factorial*i 
			lst.append(factorial) 
		print lst
	except Exception:
		print "....error occured...."

facto()  #function call