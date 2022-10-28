// A. Multiplication Table.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
int main()
{
    int n, x;
    cin >> n >> x;
    int t=0;
    for (int i = 1; i <= n; i++)
    {
        if (x%i==0 && x / i<=n)
        {
        t+=1;
        }
    }
    cout << t << endl;
    return 0;
}