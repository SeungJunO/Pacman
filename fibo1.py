import time


def fib1(n):
    a,b,=0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b

def fib2(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

start = time.time()
fib1(100000)
end = time.time()
print(end - start)
