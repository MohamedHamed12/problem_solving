#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while (t--)
    {
       int n;string a;
       cin>>n;
       cin>>a;
       int fl=0;int sl=0;

       for (int i = n-1; i >=0 ; i--)
       {
         if (a[i]=='1')
         {
            fl=i+1;
            break;
         }
         
       }
        for (int i = 0; i <n ; i++)
       {
         if (a[i]=='1')
         {
            sl=n-i;
            break;
         }
         
       }
       if(fl==0 && sl==0) cout<<n<<endl;
       else 
       {
         if (fl>sl)
         {
           cout<<2*fl<<endl;;
         }
         else
         {
           cout<<sl*2<<endl;;
         }
         
       }

    }
    

    return 0;
}