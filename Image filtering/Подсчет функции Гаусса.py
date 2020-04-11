import math
sigma,x,y = map(int,input().split())
res = (1/(2*math.pi*(sigma**2)))*math.exp((-x**2-y**2)/(2*(sigma**2)))
print(res)
