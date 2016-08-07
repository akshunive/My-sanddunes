''' Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.'''

list=input("enter the list of numbers:")
print len(list) #to find the length of the list
print list[-1]  #to print the last item in list
print list[::-1] #to print the list in reverse
if(list.count(5)==0): # Print Yes if the list contains a 5 and No otherwise
     print "no"
else:
     print "yes"
print list.count(5)  #to print the number of 5's in list
