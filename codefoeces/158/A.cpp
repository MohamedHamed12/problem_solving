#include <iostream>
#include "string"
using namespace std;

int main()
{
	int n, k;
	cin >> n >> k;

	int o;
	for (int i = 0; i < k; ++i)
	{
		cin >> o;
		if (o == 0)
		{
			cout << i << endl;
			return 0;
		}
	}

	int p;
	for (int i = k; i < n; ++i)
	{
		cin >> p ;
		if (p != o)
		{
			cout << i << endl;
			return 0;
		}
	}

	cout << n << endl;
	return 0;
}