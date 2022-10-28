#include <iostream>
#include "string"
using namespace std;
int main()
{
	int s,h,m,n,g,t;
	m =n= 0;
	s = 5;
	g = 0;
	while(s--)
	{
		for (h = 1; h <= 5; h++)
		{
			cin >> g;
			if (g == 1)
			{
				m = 5-s;
				n = h;
			}
		}
	}
	t = abs(m - 3) + abs(n - 3);
	cout << t << endl;
}