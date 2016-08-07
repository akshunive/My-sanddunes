#to find missing number comparing two arrays
list1=[1,2,3,4,5]
list2=[2,3,1,0,5]
n=(set(list1)-set(list2)) #to find missing terms in list2
m=(set(list2)-set(list1)) #to find missing terms in list1
print "missing in list2=",n,"missing in list1=",m

