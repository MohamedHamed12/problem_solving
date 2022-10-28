
#include <iostream>
#include "string"
using namespace std;
int main()
{
	string a,b,c;

	int n, t;
	cin >> n>> t;
	cin >> a;

	while (t--)
	{

		for (int i = 0; i < n; i++)
		{
			
			if (a[i] == 'G' && a[i - 1] == 'B')
			{
				a[i] = 'B';
				a[i - 1] = 'G';
				i = i + 1;
			}
		}
		
	}
		cout << a << endl;
}