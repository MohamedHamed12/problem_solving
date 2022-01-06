#include <stdio.h>
#include <string.h>
#include <stdbool.h>
char *gett(char *a)
{
   int m=0;
  
   for (int i = 0; i < strlen(a); i++)
     {
        if (a[i]!='?')
        {
           
         if(a[0]=='?' &&m==0)  m=i;
          
           while (a[i+1]=='?')
           {
             if (a[i]=='R')  a[i+1]='B';
              
             
             else if (a[i]=='B') a[i+1]='R';  
           }
           
           
        }
       
        
        
     } 
      if (a[0]=='?' && m==0) a[strlen(a)-1]='R';
     for (int i = m; i >-1 ; i--)
     {
        
        
           while (a[i-1]=='?')
           {
             if (a[i]=='R')  a[i-1]='B';
              
             
             else if (a[i]=='B')  a[i-1]='R';  
           }
           
           
        
        
     } 
     if (a[0]=='?')
     {
        if (a[1]=='R')  a[0]='B';
              
             
             else if (a[1]=='B')  a[0]='R';  
     }

    return a;
}




int main(){
int t;
scanf("%d",&t);
int n;
char a[10000];
char d[10000];
  while (t--)
  {
     scanf("%d",&n);
     scanf("%s",&a);
     printf(gett(a));
     printf("\n");

 
     
     

  }
  return 0;
}