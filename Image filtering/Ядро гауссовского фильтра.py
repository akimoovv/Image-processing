import math

def gaus(sigma,x,y):
    return (1/(2*math.pi*(sigma**2)))*math.exp((-x**2-y**2)/(2*(sigma**2)))
def f(sigma):
    K = int(round(6 * sigma)+1)
    Sum = 0
    K_array = [[0]* K for _ in range(K)]
    
    for i in range(K):
        for j in range(K):
            x = j - K//2
            y = (-i) + K//2
            K_array[i][j] = gaus(sigma, x, y)
            Sum += K_array[i][j] 
    for i in range(K):
        for j in range(K):
            x = K_array[i][j]/Sum
            K_array[i][j] = float('{:.5f}'.format(x))
    return K_array

sigma = float(input())
array = f(sigma)

for i in range(len(array)):
    print(*array[i])
