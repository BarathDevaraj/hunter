n=int(input())
d=list(map(int,input().split()[:n]))
count=0
for i in range(n):
	for j in range(i+1,n):
		if (d[i]+d[j]==0):
			print(d[i],end=' ')
			print(d[j])
			count=1
if(count==1):
	for i in range(n):
		for j in range(i+1,n):
			if (d[i]+d[j]==-1 or d[i]+d[j]==1):
				print(d[i],end=' ')
				print(d[j])
				
