n=int(input())

c=list(map(int,input().split()))
x=sorted(c)
mid=len(x)//2
print(x[mid])
