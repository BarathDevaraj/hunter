n=int(input())
d=list(map(int,input().split()[:n]))
count=0
for i in range(n):
	if d[i]==i:
		print(d[i],end=' ')
		count=1
if(count==0):
	print('-1')
