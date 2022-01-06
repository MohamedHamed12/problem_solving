#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int getmoves (int a0,int a1,int a2,int m)
{
   int tot=0;
  if (a0>=a1 &&a0>=a2)
  {
      tot+=a0-m;
  a1+=a0-m;
  if (a1>m) 
  {tot+=a1-m;
  a2+=a1-m;}
  if (a2>m) 
  {tot+=a2-m;
  a0+=a2-m;}
  if (a0>m) tot+=a0-m;
 }
  else if (a1>=a0 &&a1>=a2)
  {
     tot+=a1-m;
      a2+=a1-m;
  if (a2>m) 
  {tot+=a2-m;
   a0+=a2-m;}
  if (a0>m)
  { tot+=a0-m;
   a1+=a0-m;}
  if (a1>m) tot+=a1-m;
  }
  else if (a2>=a0 &&a2>=a1)
  {   
    tot+=a2-m;
    a0 += a2-m;
  if (a0>m)
  {
    tot+=a0-m;
  a1+=a0-m;
  }
  if (a1>m) 
  {
    tot+=a1-m;
   a2+=a1-m;
  }
  if (a2>m) tot+=a2-m;
  }
   return tot;
}
/* int comparator (const void * p1, const void * p2)
{
  return (*(int*)p1 - *(int*)p2);
} */
int main(){
  int t;
  scanf("%d",&t);
  while (t--)
  {
    int n;
   scanf("%d",&n);
   int a [n];
   int a0=0 ,a1=0,a2=0;
   for (int i = 0; i < n; i++)
   {
    scanf("%d",&a[i]);
    if (a[i]%3==2) a2 ++;
    else if (a[i]%3==1) a1++;
    else  a0 ++;
   }
  /*   qsort(b, 3, sizeof(int), comparator); */
    int m=n/3;
 int result =getmoves(a0,a1,a2,m);
   printf("%d\n",result);
  }
    return 0;
}