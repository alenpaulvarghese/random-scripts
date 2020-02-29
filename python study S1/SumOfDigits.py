n=input("enter")
reverse=0
while(n>0):
	re=n%10
	reverse=reverse+re
	n=n/10
print reverse
