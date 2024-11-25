N = int(input())
L = int(input())

def func(N,L):
    num = 0
    for i in range(1,N+1,1):
        num += L%10
        L = L//10
    return num

print(func(N,L))
