

#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n;
	int a, b, c,x,y,z;
	x = y = z = 0;
	cin >> n;
	while (n--)
	{
		cin >> a >> b >> c;
		x += a;
		y += b;
		z += c;
	}
	if (x == 0 && y == 0 && z == 0)
	{
		cout << "YES" << endl;
		return 0;
	}
	else
	{
		cout << "NO" << endl;
		return 0;
	}
}