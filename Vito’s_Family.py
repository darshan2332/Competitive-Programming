n=int(input()) 
for i in range(0,n): 
    dist=0 
    a=list(map(int,input().split())) 
    for i in range(1,len(a)): 
        if i==len(a)-1:
dist+=0 
        else:
dist+=abs(a[i+1]-a[i]) 
    print(dist) 
