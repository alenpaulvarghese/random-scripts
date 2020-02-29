x=input('Enter no')
if(x%100==0):
	if (x%400==0):
		print "the year is leap and century year"	
	else:
		print "the year is century year"
elif(x%4==0):
	print "the year is leap year"
else:
	print "not both"

 
