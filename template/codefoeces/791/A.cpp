

#include <iostream>
#include "string"
using namespace std;
int main()
{
	int a, b,c,d,n;
	cin >> a >> b;
	c = a;
	d = b;
	n = 0;
	while (d>c)
	{
		d = d * 2;
		c = c * 3;
		n += 1;

	}
	if (d == c)
	{
		n += 1;
	}
	cout << n << endl;
	return 0;
}