def quick_power(num, a): #num^a
    if a == 0: return 1
    if a == 1: return num
    if a == -1: return 1/num
    
    res = quick_power(num, a//2) ** 2
    if a % 2 == 1:
        res *= num
    return res

print(quick_power(2, 10))