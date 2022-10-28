

#include <iostream>
#include "string"
using namespace std;
int main()
{
	int a, b, c, t;

	cin >> a>> b>> c;

	t = a*c*(c+1 )/2;

	if (t - b>=0)
	{
		cout << t - b << endl;
	}
	else
	{
		cout << 0 << endl;
	}
	return 0;

}