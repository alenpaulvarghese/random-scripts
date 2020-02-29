n=input("Enter")
r=0
while(n>0):
	reverse=n%10
	r=r*10+reverse
	n=n/10
print r
