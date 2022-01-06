#include <stdio.h>
int main(){
  int n,k,min,nOfMin;
  scanf("%d %d",&n,&k);
  int a[10000];
  
  for (int i = 0; i < n; i++)
  {
   scanf("%d",&a[i]);
  }
  int com=0,tot=0;
    
    for (int i = 0; i < n; i++)
   {
     if(a[i]<com)
     {
       tot+=com-a[i];
       a[i]=com;
     }
     if (a[i]<k)
     {
       com=k-a[i];
     }
     else com=0;
   }
   
   printf("%d\n",tot);
  for (int i = 0; i < n; i++)
    {
      printf("%d ",a[i]);
    }
  
  
   
   
   
   
  

    return 0;
}