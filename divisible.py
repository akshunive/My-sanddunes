#to print the numbers between 2000 to 3200 which are divisible by 7 and not by 5  
lst=[]
def divisible():
	try: 
		for i in range(1999,3201):  #checking in the given range
			if(i%7==0) and not(i%5==0):   #to check i is divisible by 7 and not by 5    
				lst.append(i)
		print lst
	except Exception:         #exception occured
		print "error"

divisible()
