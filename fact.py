#to find the sum of the factorials of two numbers
num_1=input("enter the first num:")
num_2=input("enter the second num:")
factorial_1=1
factorial_2=1
for i in range(1,num_1+1):
	factorial_1=factorial_1*i #factorial of first number  
for i in range(1,num_2+1):
	factorial_2=factorial_2*i  #factorial of second number

factorial=factorial_1+factorial_2 #sum of factorial of two numbers
print "factorial:",factorial
 