n=list(map(int,input().split(",")))
for i in range(0,len(n)):
	fact=1
	for j in range(0,n[i]):
		f=n[i]-j
		fact=f*fact
	print(fact,end=",")
