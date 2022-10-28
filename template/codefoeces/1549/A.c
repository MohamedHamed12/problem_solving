#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        bool b=false;
        int i=1;
        int num;
        while (b==false)
        {
            i++;
            num=n-1;
    for (i ; i <= num; ++i) {
        if (num % i == 0) {
                printf("%d %d\n",i,num);
        b=true;
        break ;
        }
    }
   ;
}

        }


    return 0;
}