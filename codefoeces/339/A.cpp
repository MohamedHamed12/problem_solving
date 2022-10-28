
#include <iostream>
#include "string"
using namespace std;

int main()
{
	string a, b1, b2, b3, b4;
	int i;
	cin>> a;
	for (i = 0; i < a.length();i++)
	{
		if (a[i] == '1')
		{
			b1 += a[i];
			b1 += '+';
		}
		 if (a[i] == '2')
		{
			b2 += a[i];
			b2 += '+';
		}
		if  (a[i] == '3')
		 {
			b3 += a[i];
			b3 += '+';
		}
		

	}

	b4 = b1 + b2 + b3;
	b4.erase(b4.begin() + b4.length() - 1, b4.end());
	cout <<b4 << endl;
}