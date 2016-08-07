#to print the number and its square value in dictionary format i.e., key and value format
num=input("enter the num:")

def compute(num):
	count=1
	d={}
	d2={}
	while (count<=num):
		d2={count:count*count} #store the value of count and its square in a dictionary
		d.update(d2)           #update the dictionary with values   
		count=count+1        
	print d

compute(num)
	