n,s=map(int,input().split())
c=0
for i in range(n+1,s):
    if(i%2==0):
        
       if c==0:
           print (i)
           c=c+1
       else:
           print(i.end=" ")
