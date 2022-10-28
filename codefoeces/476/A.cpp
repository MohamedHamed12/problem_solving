
#include <iostream>
using namespace std;
int main()
{
	int n, m;
	int min;
	cin >> n >> m;
	if(n%2==0)
	min = n / 2;
	else
		min = n / 2 + 1;
	while (min<=n)
	{
		if (min % m == 0)
		{
			cout << min << endl;
			return 0;
		}
		else
			min += 1;

	}
	cout << "-1" << endl;
	return 0;
}