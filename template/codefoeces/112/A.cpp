#include <iostream>
#include "string"
using namespace std;


int main()
{
	
	string a, c;
	int t, i;
	t = 0;

	cin >> a >> c;

	for ( i = 0; i<a.length();i++)
	{
		if (a[i] <= 92)
		{
			a[i] = a[i] + 32;
		}
		if ( c[i] <= 92)
		{
			c[i] = c[i] + 32;
		}

	}
	if (a < c)
	{
		cout << -1;
	}
	else if (a > c)
	{
		cout << 1;
	}
	else if (a == c)
	{
		cout << 0;

	}
	
}