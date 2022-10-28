
#include <iostream>
using namespace std;
int main()
{
	int t;
	long long  n,out,total;
	cin >> t;
	while (t--)
	{
		total = 0;
		cin >> n;
		
			while (n > 1)
			{
				out = (4 * n - 4) * (n / 2);
				total += out;
				n = n - 2;
			}
			cout << total << endl;

		

	}
	return 0;
}