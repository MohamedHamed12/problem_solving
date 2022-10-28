
#include <iostream>
using namespace std;
#include "string"
int main()
{
	string a[3000];
	string b[3000];
	string min[3000];
	string max[3000];
	string c[3000];
	string d[3000];

	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> a[i];
		cin >> b[i];

		if (a[i].length() <= b[i].length())
		{
			min[i] = a[i];
			max[i] = b[i];
		}
		else
		{
			min[i] = b[i];
			max[i] = a[i];
		}
	}

	for (int i = 0; i < n; i++)
	{
		
		cin >> c[i];
		for (int j = 0; j < m; j++)
		{
			if (c[i] == max[j])
			{
				c[i] = min[j];
			}

		}
		 
	}
	for (int i = 0; i < n; i++)
	{
		cout << c[i] << endl;
	}
	return 0;
}