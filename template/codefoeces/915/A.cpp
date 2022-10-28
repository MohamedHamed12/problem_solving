
#include <iostream>
//#include "string"
using namespace std;
int main()
{
	int n, l,b;
	b = 0;
	cin >> n >> l;
	int a[1000];

	for (int i=0;i<n;i++)
	{
		cin >> a[i];
		if (l % a[i] == 0 &&a[i]>b)
		{
			b = a[i];
		}

	}
	cout << l / b << endl;
}