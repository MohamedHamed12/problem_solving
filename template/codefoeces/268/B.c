#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,sum;
    sum=0;
    scanf("%d",&a);
    for(int i=0;i<a;i++)
    {
        sum+=(a-i)*(i+1)-i;
    }
    printf("%d",sum);
    return 0;
}