#to implement the class concept to print the given username and password of the user if the password contains both numbers and char
class Gmail:
	def __init__(self,u,p):
		self.username=u
		self.password=p
	
	def display(self):
		if not self.password.isdigit():
			if not self.password.isalpha():
				print "username:",self.username
				print "password:",self.password
		else:
			print "password should contain both digit and char"


u=raw_input("enter the username:")
p=raw_input("enter the password:")
user_1=Gmail(u,p)
user_1.display()
