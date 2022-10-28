
#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n,b,c;
	c =0;
	b = 0;
	cin >> n;
	int a[100000];
	cin >> a[0];
	for (int i=1;i<n;i++)
	{
		cin >> a[i];
		if (a[i] >= a[i -1])
		{
			b += 1;
		}
		else
		{
			b = 0;
		}
		if (b > c)
		{
			c = b;
		}
	}
	cout << c+1 << endl;
	return 0;
}