#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, a,b;
    scanf("%d%d%d",&n,&a,&b);
    if(n-a>=b+1)
         printf("%d",b+1);
    else
         printf("%d",n-a);
    return 0;
}