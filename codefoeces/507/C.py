


######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
h, ext = map(int, input().split());
root = 0;
tem = 0;
lft = True;
 
while(h >= 1):
    h-= 1;
    if(ext > tem and ext <= tem + (pow(2,h))):
        if(lft):
            root += 1;
            lft = not lft;
        else:
            root += (pow(2,h+1));
    else:
        tem += pow(2,h);
        if(not lft):
            root += 1;
            lft = not lft;
        else:
            root += (pow(2,h+1));
 
print(f"{root}");