a=".|."
heigt,width=map(int,input().split())

for i in range(int(heigt/2)):
    print((((i+1)*2-1)*a).center(width,"-"))
print("WELCOME".center(width,"-"))
for i in range(int(heigt/2)-1,-1,-1):
    print((((i+1)*2-1)*a).center(width,"-"))