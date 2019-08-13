n=int(input())
d=list(map(int,input().split()[:n]))
for i in range(n):
	if (d[i]%2==0 and i%2==1)or(d[i]%2==1 and i%2==0):
		print(d[i],end=' ')
