#include <iostream>
using namespace std;
int main()
{
	int x, n,t;
	n = 1;
	t = 0;
	cin >> x;
	while (x !=0)
	{
		if (x % 2 != 0)
		{
			x = x - 1;
			t += 1;
		}
		x = x / 2;
	}
	cout << t << endl;
	return 0;
}