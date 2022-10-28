#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <forward_list>
#include <utility>
#include <set>
#include <unordered_set>
#include <map>
#include <queue>
#include <iomanip>  
using namespace std;
typedef signed long long ll;

int main()
{

    ll t, k, x;
    cin>>t;
    for (ll i = 0; i < t; i++)
    {
        cin >> k >> x;
        ll sumk = k * (1 + k) / 2;
        if (x <= sumk)
        {
            
          cout<<fixed<<setprecision(0)<<ceil((-1 + sqrt(1 + 8*x)) / 2) ;
          

        }
            
        else
        {
            x -= sumk;
            ll y = 2 * k - 1;
           
            if (y*y - (8 * x) >= 0)
            {
            ll tem=ceil((y-sqrt(y*y-(8*x)))/2);
           cout<<fixed<<setprecision(0)<<((tem + k));
            }
            else
                {cout<<fixed<<setprecision(0)<<(2 * k - 1);}
        }
        cout<< endl;
    }
        return 0;
}