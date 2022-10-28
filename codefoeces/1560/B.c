#include <stdio.h>
#include <string.h>
void order (int*a,int*b)
{
    if (*a<*b)
    {
        int tem;
        tem=*a;
        *a=*b;
        *b=tem;
    }  
}
 int postion (int c,int m)
{
    if (c>m)
    return -1;
    else if(c<=m/2 &&c>0)
    {
        int tem=c+(m/2);
       return tem;
    }
    else if(c>m/2)
    {
        int tem=c-m/2;
        return tem;
    }
}
int main(){
int t;
scanf("%d",&t);
  while (t--)
  {
      int a,b,c,totnum;
      scanf("%d %d %d",&a,&b,&c);
      order(&a,&b);
      totnum=(a-b)*2;
      if (totnum<a)
      printf("-1\n");
      else
      printf("%d\n",postion(c,totnum));
  }
  return 0;
}