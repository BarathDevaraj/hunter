n=int(input())
d=list(map(int,input().split()[:n]))
for i in range(n):
	for j in range(i+1,n):
		if (d[i]+d[j]==0):
			print(d[i],end=' ')
			print(d[j])
