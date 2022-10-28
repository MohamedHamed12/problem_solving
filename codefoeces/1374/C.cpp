
#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n,max;
	max = 0;

	int m;

	int r, l;
	r = l = 0;
	string a;
	cin >> n;
	while (n--)
	{
		max = 0;

		cin >> m;
		cin >> a;
		for (int i = 0; i < m; i++)
		{
			if (a[i] == '(')
			{
				r += 1;
			}
			if (a[i] == ')')
			{
				l += 1;
			}
			
			if (max < l - r)
			{
				max = l - r;
			}
		}
		cout << max << endl;
		
	}
	return 0;
}