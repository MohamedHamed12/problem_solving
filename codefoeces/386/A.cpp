
#include <iostream>

#include "string"
using namespace std;


int main()
{
	int n, b, m, s;
	b = 0;
	s = 0;
	cin >> n;
	int a[1000];
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
		if (b < a[i])
		{
			s = b;
			b = a[i];
			m = i + 1;
		}
		if (b > a[i]&&a[i]>s)
		{
			s = a[i];
		}

	}
	

	cout << m << " " << s << endl;

}