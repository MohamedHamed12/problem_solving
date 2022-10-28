#include <stdio.h>
#include <math.h>
#include <string.h>
int main(){
int t;
scanf("%d",&t);
  while (t--)
  {
      int n=0,row=0,colum=0;
      scanf("%d",&n);
      int tem=sqrt(n);
      int remain=n-tem*tem;
      if (remain==0)
      {
          row=tem;
          colum=1;
      }
      else if (remain>tem+1)
      {
          row=tem+1;
           remain-=(tem+1);
           colum=tem-remain+1;


      }
      else
      {
          colum=tem+1;
          row=remain;
      }
      printf("%d %d\n",row,colum);
  }
  return 0;
}