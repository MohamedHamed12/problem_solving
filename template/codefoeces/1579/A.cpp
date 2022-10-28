 #include <iostream>

using namespace std;
void solve( ) 
{
        string s; 
        cin>>s;
        int a=0;
        int b=0; 
        int c=0; 
        for( int i=0;i<s.size() ;i++) 
        {
          if(s[i]=='A') a++;
          else if(s[i]=='B')
          b++;
          else
          c++;

        }
        int d=a+c;
         
       if (d==b)
       {
        cout<<"YES"<<"\n" ;
       }
       else
       cout<<"no"<<"\n" ;
       return ;
}


int main() 
{
  int t; 
  cin>>t;
  while ( t--) 
  solve( ) ; 
  return 0;
 }