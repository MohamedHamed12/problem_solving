#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<math.h>
int LCM(int a,int b)
{
    int t;
    if(a>b)
        t=b;
    else
        t=a;
    while(t%a!=0||t%b!=0)
        t++;
    return t;
}
int min(int a,int b)
{
    if(a>b)
        return b;
    else
        return a;
}
int main()
{
    char a[80000],b[80000],c[80000],d[80000];
    int l1,l2,l;
    int n,i,j,k;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%s%s",a,b);
        l1=strlen(a);
        l2=strlen(b);
        k=LCM(l1,l2);
        l=min(l1,l2);
        strcpy(c,a);
        strcpy(d,b);
        for(i=1; i<k/l1; i++)
        {
            strcat(c,a);
        }
        for(i=1; i<k/l2; i++)
        {
            strcat(d,b);
        }
        for(i=0; i<k; i++)
        {
            if(c[i]!=d[i])
                break;
        }
        if(i<k)
            printf("-1\n");
        else
            printf("%s\n",c);
    }
    return 0;
}