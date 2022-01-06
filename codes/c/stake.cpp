# include <iostream>
#include <stack>
#include <stdbool.h>
using namespace std;

int main(){
   int t;
   cin>>t;
   string a;
    bool b;
    
   while (t-- )
   { 
       int tot=0;
      bool b =true;
       stack<char>s;
     cin>>a;
     if ((a.length())%2==0)
     {

     
         for (int i = 0; i < a.length(); i++)
     {
           if (a[i]=='(') s.push(a[i]);
           else if (a[i]==')')
           {    if (tot>0) tot--;
               else if(s.empty()!=true) s.pop();
               else
               {
                     b=false;
                     break ;
               }
           }
           else if (a[i]=='?')
           {
                
                tot++ ;
           }
     }
     }   
     else b=false;
     
     if ( (s.size()+tot)%2==0&& a[a.length()-1]!='('  && b==true )  printf("YES\n");
     else printf("No\n");
   }
   return 0;
}
   
    