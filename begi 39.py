
t=list(map(int,input().split()))

w=t[0]
t=t[1]
w=w^t
t=t^w
w=w^t
print(w,t)
