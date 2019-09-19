

def quick_power(num, a): #num^a
    if a == 0: return 1
    if a == 1: return num
    if a == -1: return 1/num
    
    res = quick_power(num, a//2) ** 2
    if a % 2 == 1:
        res *= num
    return res

def quick_power2(x: float, n: int) -> float:      
    judge = True
    if n < 0:
        n = -n
        judge = False      
    final = 1
    while n>0:
        if n & 1:   #代表是奇数
            final *= x
        x *= x
        n >>= 1     # 右移一位
    return final if judge else 1/final


import time
stime = time.time()
print(quick_power(500, 100))
print(time.time()-stime)

stime = time.time()
print(quick_power2(500, 100))
print(time.time()-stime)