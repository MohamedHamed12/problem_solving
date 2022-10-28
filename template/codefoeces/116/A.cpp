
#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n;
	int a, b;
	int t,c;
	c = t = 0;
	cin >> n;
	while (n--)
	{
		cin >> a >> b;
		t =t- a;
		t = t + b;
		if(t>c)
		{
			c = t;
		}
	}
	cout << c << endl;
	return 0;
}