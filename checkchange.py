a,b=map(str,input().split())
c=0
for i in range(0,len(a)):
      for j in range(0,len(b)):
            if i==j:
                  if a[i]!=b[j]:
                        c+=1
if c==1:
      print('yes')
else:
      print('no')
            
