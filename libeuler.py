import time
import math

# integer square root:

def isqrt1(n):
    x = n
    y = (x + n//x) >> 1
    # print('x = {}, y = {}'.format(x, y))
    while y < x:
        x = y
        y = (x + n//x) >> 1
        # print('x = {}, y = {}'.format(x, y))
    return x

def isqrt2(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y    

def isqrt3(n):
    a, b = divmod(n.bit_length(), 2)
    bit = 2**(a+b)
    x = 0
    while bit != 0:
        tmp = x | bit
        if tmp*tmp <= n:
            x = tmp
        bit >>= 1
    return x

if __name__ == "__main__":
    # test wich version is fastest
    t = time.process_time()
    for n in range(1, 10000):
        if math.floor(math.sqrt(n)) != isqrt1(n):
            print(n)
    elapsed_time = time.process_time() - t
    print('time: ', elapsed_time)
    t = time.process_time()
    for n in range(1, 10000):
        if math.floor(math.sqrt(n)) != isqrt2(n):
            print(n)
    elapsed_time = time.process_time() - t
    print('time: ', elapsed_time)
    t = time.process_time()
    for n in range(1, 10):
        if math.floor(math.sqrt(n)) != isqrt3(n):
            print(n)
    elapsed_time = time.process_time() - t
    print('time: ', elapsed_time)
