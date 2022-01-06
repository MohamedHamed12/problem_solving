#include <stdio.h>
#include <string.h>


int main(){
  
  
     int n=0,k=0,min,nOfMin;
     scanf("%d %d",&n,&k);
     int a[1000];
      scanf("%d",&a[0]);
       scanf("%d",&a[1]);
      min=a[1];
     for (int i = 2; i < n; i++)
     {
       scanf("%d",&a[i]);

       if (i<n-1 &&min>a[i])
       {
         min=a[i];
         nOfMin=i;
       }
       
     }
     if (n)
     {
       /* code */
     }
     
     int tem=smallOfTwo(k,a[nOfMin+1],a[nOfMin-1]);
     for (int i = nOfMin; i < n; i++)
     {
      
     }
     for (int i = 0; i <nOfMin; i++)
     {
      
     }
     
   
     
         
     
    
     

    return 0;
}