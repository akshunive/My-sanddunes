#exception handling
a=input("enter a:")
b=input("enter b:")
try:
	c=a/b
	print c

except Exception:
	print "b cannot be 0"