

#include <iostream>
using namespace std;
int main()
{
	int t, n, m;
	int tem;
	cin >> t;
	for (int  i = 0; i < t; i++)
	{
		cin >> n >> m;
		tem = m * n;

		if (tem % 2 == 0)
		{
			cout<<( tem / 2)<<endl;
		}
		else
		{
			cout << ( (tem + 1) / 2) << endl;
		}
	}
	return 0;
}