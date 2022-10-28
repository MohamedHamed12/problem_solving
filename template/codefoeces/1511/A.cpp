#include <iostream>
using namespace std; 
int main()
{
	int t, a, tem, n;

	cin >> t;
	while (t--)
	{
		tem = 0;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> a;
			if (a == 1 || a == 3)
			{
				tem += 1;
			}
		}
		cout << tem << endl;
	}
	return 0;

}