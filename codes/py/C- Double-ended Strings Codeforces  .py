def first(firstStr,secondStr):
    global Commenlen
    for i in range(len(secondStr)):
        for j in range(len(secondStr)):
            if secondStr[:len(secondStr)-1-j]  in firstStr :
                Commenlen.append(len(secondStr)-1-j)
                break
        
        secondStr=secondStr[i:]

def second(firstStr,secondStr):
    global Commenlen
    for i in range(len(secondStr)-1,-1,-1):
        for j in range(len(secondStr)):
            if secondStr[j:]  in firstStr :
               Commenlen.append(len( secondStr[j:]))
               break
        secondStr=secondStr[:i]

for i in range(int(input())):
    Commenlen=[]
    Commenlen.append(0)
    str1=input().strip()      ;str2=input().strip()

    first(str1,str2)    ;  first(str2,str1)
    second(str1,str2)   ;  second(str2,str1)

    print((len(str1)+len(str2))-max(Commenlen)*2)
