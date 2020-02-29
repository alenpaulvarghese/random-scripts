n=input("enetr")
r=0
q=n
while(n>0):
	reverse=n%10
	r=r*10+reverse
	n=n/10
print r

if(r==q):
	print "the palidrome bich"
else:
	print "no u"
