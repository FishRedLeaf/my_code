# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:48:52 2019

@author: 鱼红叶

https://zhidao.baidu.com/question/711748456351770685.html

要求使用图论法对该问题建模，地图视为无向图，对其用邻接矩阵表示，0表示两省份不相邻，
1表示两省份相邻，总共七个省份，1,2,3,4四种颜色

要求输入矩阵 0100001
1011111
0101000
0110100
0101010
0100101
1100010
要求输出 1213134
"""

def FourColorLabel(GuanXiJuZheng):
    Num=len(GuanXiJuZheng)
    Color=[-1 for i in range(Num)]
    n=m=1
    #染色第一个区域，先设置为1
    while m<=Num:
        while n<=4 and m<=Num:
            flag=True
            for k in range(m-1):
                if GuanXiJuZheng[m-1][k]==1 and Color[k]==n:
                    flag=False    #染色有冲突
                    n+=1
                    break    
            if flag:
                Color[m-1]=n;
                m+=1
                n=1
        if n>4:                 # 超出标记范围 必须回退
            m-=1
            n=Color[m-1]+1
    return Color
 
GuanXiJuZheng=[
                [0,1,0,0,0,0,1],
                [1,0,1,1,1,1,1],
                [0,1,0,1,0,0,0],
                [0,1,1,0,1,0,0],
                [0,1,0,1,0,1,0],
                [0,1,0,0,1,0,1],
                [1,1,0,0,0,1,0]
             ]
for i in FourColorLabel(GuanXiJuZheng):
    print(i)