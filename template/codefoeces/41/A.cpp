
#include <iostream>
#include "string"
using namespace std;
int main()
{
	string a,b,c;
	cin >> a>>c;
	
	for (int i = 0; i < a.length(); i++)
	{
		if (c[i] == a[(a.length()) - i - 1])
			continue;
		else
		{
			cout << "NO" << endl;
			return 0;
		}
	}

		cout << "YES" << endl;
		return 0;
	
	
}