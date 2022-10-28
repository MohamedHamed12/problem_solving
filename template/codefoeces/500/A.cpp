
#include <iostream>
using namespace std;
int main()
{
	int n,t;
	int tem=1;
	cin >> n >> t;
	int a[30000];
	int b[30000];
	for (int i = 1; i < n; i++)
	{
		cin >> a[i];

		b[i] = a[i] + i;
	}
	while (tem<n)
	{
		

		if (b[tem] == t)
		{
			cout << "YES" << endl;
			return 0;
		}
		tem = b[tem];
	}
	cout << "NO" << endl;
	return 0;
}