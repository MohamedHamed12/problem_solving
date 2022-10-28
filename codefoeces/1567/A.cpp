#include <iostream>

using namespace std;

int main()
{
   int t;
   cin>>t;
   while (t--)
   {
      int n;
      cin>>n;
      string a;
      cin>>a;
      for (int  i = 0; i < n; i++)
      {
          if (a[i]=='D')
          {
             a[i]='U';        
          }
          else if (a[i]=='U')
          {
             a[i]='D';
          }
       }
       cout<<a<<endl;;
   
}
 return 0;
}