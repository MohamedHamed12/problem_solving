
#include <iostream>
using namespace std;
int small(int x, int y)
{
    if (x < y)
        return x;
    else 
        return y;
}
int main()
{
    long long t;
    long long  x, y;
    long long a, b;
    long long total,tem;
    
    cin >> t;
    while (t--)
    {
        total = 0;
        cin >> x >> y;
            cin>>a>>b;
        if (2 * a >= b)
        {
            tem = small(x, y);
           
            total += b * tem;
            x = x - 1*tem;
            y = y - 1*tem;
           
            
            tem = x + y;
            total += tem * a;
            
           
        }
        else
        {
            tem = small(x, y);
            total += 2 * a*tem;
            x = x - 1 * tem;
            y = y - 1 * tem;
            
            
            tem = x + y;
            total += tem * a;
           
        }
        cout << total << endl;


    }
    return 0;

}