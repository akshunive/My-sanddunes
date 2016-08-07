#to calculate the salary hike
salary=input("enter the salary:")
salary=float(salary)
percentage=0
if(0.00<salary<400.00):
	hike=salary*0.15
	newsalary=hike+salary
	percentage="15%"
if(400.01<salary<800.00):
	hike=salary*0.12
	newsalary=hike+salary
	percentage="15%"
	percentage="12%"
if(800.01<salary<1200.00):
	hike=salary*0.10
	newsalary=hike+salary
	percentage="15%"
	percentage="10%"
if(1200.01<salary<2000.00):
	hike=salary*0.07
	newsalary=hike+salary
	percentage="7%"
print "Novo salario:",float(newsalary)
print "Reajuste ganho:",float(hike) 
print "Em percentual:",percentage
