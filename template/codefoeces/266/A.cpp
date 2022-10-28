

#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n,t; 
	t = 0;
	cin >> n;
	char ar[50];
	cin >> ar;
	char m;
	m = ar[0];
	for (int i = 1; i <= n; i++)
	{
		if (ar[i] == m)
		{
			t += 1;
		}
		m = ar[i];
	}
	cout << t << endl;
}