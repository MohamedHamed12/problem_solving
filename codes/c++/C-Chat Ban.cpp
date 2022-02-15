/* codeforces*/

#include <iostream>
#include <iomanip>  
#include <math.h> 
using namespace std;
 
int main()
{
 
    long long t, k, x;
    cin>>t;
    for (long long i = 0; i < t; i++)
    {
        cin >> k >> x;
        long long sumk = k * (1 + k) / 2;
        if (x <= sumk)
        {   
          cout<<fixed<<setprecision(0)<<ceil((-1 + sqrt(1 + 8*x)) / 2) ;
        }   
        else
        {
            x -= sumk;
            long long y = 2 * k - 1;
            if (y*y - (8 * x) >= 0)
            {
            long long tem=ceil((y-sqrt(y*y-(8*x)))/2);
           cout<<fixed<<setprecision(0)<<((tem + k));
            }
            else
                {cout<<fixed<<setprecision(0)<<(2 * k - 1);}
        }
        cout<< endl;
    }
        return 0;
}
 
 /*https://codeforces.com/problemset/submission/1612/146217011*/
