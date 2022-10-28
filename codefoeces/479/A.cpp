
#include <iostream>
using namespace std;
int main()
{
    int a, b, c,t;
    cin >> a>> b>>c;
    t = a+b+c;
    if (a * b * c > t)
    {
        t=a* b* c ;
    }
    if (t<(a + b) * c )
    {
        t = (a + b) * c;
    }
    if (t < a + b * c)
    {
        t = a + b * c;
    }
    if (t < a * b + c)
    {
        t = a * b + c;
    }
    if (t < a *( b + c))
    {
        t = a * (b + c);
    }
    cout << t << endl;
    return 0;
}