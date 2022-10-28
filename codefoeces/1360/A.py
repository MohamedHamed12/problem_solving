import math
for i in range(int(input())):
    rectLen,rectWidth=map(int,input().split()) 
    print(pow(max(max(rectLen,rectWidth),min(rectLen,rectWidth)*2),2))
    
#simplfiy
# import math
# for i in range(int(input())):                          #for i in range(t)
#     rectLen,rectWidth=map(int,input().split())         #input lenth and width of rectangel

#     shapeLen=max(rectLen,rectWidth) ;shapewidth=min(rectLen,rectWidth)*2

#     squreLen=max(shapeLen,shapewidth)

#     print(pow(squreLen,2))