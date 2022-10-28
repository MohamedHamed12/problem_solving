#include <stdio.h>
#include <string.h>
int main(){
int t;
scanf("%d",&t);
  while (t--)
  {
      long long  a,b,c,m=-1,n=-1;
      scanf("%lld %lld %lld",&a,&b,&c);

       if(a < c){
            m = 1;
        }
        if(a*b > c){
            n = b;
        }
      printf("%lld %lld\n",m,n);


      
          

      
      
      








   
  }
  
    return 0;
  }