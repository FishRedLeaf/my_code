
"""
https://blog.csdn.net/lishuhuakai/article/details/9133961
https://www.cnblogs.com/jamespei/p/5425950.html
"""

from math import sqrt

def nearest_dot(s):
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    mid_x = (left[-1][0]+right[0][0])/2
    
    lmin = nearest_dot(left) if len(left) > 2 else left
    rmin = nearest_dot(right) if len(right) > 2 else right
    dis_l = get_distance(lmin) if len(lmin) > 1 else float('inf')
    dis_r = get_distance(rmin) if len(rmin) > 1 else float('inf')
    d = min(dis_l, dis_r)   #最近点对距离

    mid_min=[]
    for i in left:
        if mid_x-i[0] <= d :   #如果左侧部分与中间线的距离<=d
            for j in right:
                if abs(i[0]-j[0])<=d and abs(i[1]-j[1])<=d:
                    if get_distance((i,j)) <= d: 
                        mid_min.append([i,j])
    if mid_min:
        dic=[]
        for i in mid_min:
            dic.append({get_distance(i):i})
        dic.sort(key=lambda x: x.keys())
        return list(dic[0].values())[0]
    elif dis_l > dis_r:
        return rmin
    else:
        return lmin

# 求点对的距离
def get_distance(min_points):
    p1, p2 = min_points
    return sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)

def divide_conquer(s):
    s.sort(key = lambda x : (x[0], x[1]))
    nearest_dots = nearest_dot(s)
    return nearest_dots
    
s = [(0,1),(3,2),(4,3),(5,1),(1,2),(2,1),
     (6,2),(7,2),(8,3),(4,5),(9,0),(6,4)]
print(divide_conquer(s))

    



