
#include <iostream>
using namespace std;
int main()
{
	long long t,tem;
	long long n, m;
	long long l, j;
	cin >> t;
	for (int  i = 0; i < t; i++)
	{
		cin >> n >> m;
		cin >> l >> j;
		tem = (l - n) * (j - m) + 1;
		cout << tem << endl;
	}
	return 0;
}