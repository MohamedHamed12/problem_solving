
#include <iostream>
typedef long long int ll;

#include "string"
using namespace std;
int main()
{
	int n, m,tem;
	tem = 0;
	
	cin >> n >> m;
	ll a[200000];
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
		a[i] = a[i] + tem;
		cout << a[i] / m << endl;
		tem = a[i] % m;
		

	}
	return 0;
}