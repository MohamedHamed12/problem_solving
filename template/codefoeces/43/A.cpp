
#include <iostream>
#include "string"
using namespace std;
int main()
{
	string tem;
	string a,b;
	int n ;
	int at, bt;
	at = 1;
	 bt = 0;
	cin >> n;
	cin >> a;
	n = n - 1;
	while (n--)
	{
		cin >> tem;
		if (tem == a)
		{
			at += 1;
		}
		else
		{
			b = tem;
			bt += 1;
		}
	}
	if (at > bt)
	{
		cout << a << endl;
		return 0;
	}
	else
		cout << b << endl;
	return 0;
}