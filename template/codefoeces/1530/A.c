#include<stdio.h>

int main() {

   long num ,t, r, ld = 0;
   scanf("%d", &t);
   while(t--)
   {
       ld=0;
       scanf("%d", &num);

   while (num > 0) {
       r = num % 10;
       if (ld < r) {
           ld = r;
       }
       num = num / 10;
   }
   if (ld==10)
   printf("%d\n", 1);
    else
   printf("%d\n", ld);

   }


   return 0;
}