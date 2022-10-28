for i in range(int(input())):
     if (len(set(input()).intersection(set(input())))>0 ):
         print("yes")
     else:
         print("no")