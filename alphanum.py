#finding num and alpha in a string
str="nive123"
chr=0
num=0
for i in str:
	if i.isalpha(): #to check i is char
		chr=chr+1   #if true increment char
		print i
	elif i.isdigit():#to check i is num
		num=num+1 #if true increment num
		print i
print chr,num