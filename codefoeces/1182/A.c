#include <stdio.h>
#include <math.h>

int main (){
   int a;
   scanf("%d",&a);
   if (a>0 && a%2==0)
   {
      int m=pow(2,a/2);
      printf("%lld",m);
   }
   else
   {
       printf("%d",0);
   }
   
   return 0;
}