
#include <iostream>
#include  "string"
using namespace std;
int main()
{

	string a, a2;
	cin >> a;
	int i;
	for (i = 0; i < a.length(); i++)
	{
		if (a[i] != 'a' &&a[i] != 'e' && a[i] != 'o' && a[i] != 'u' && a[i] != 'i' && a[i] != 'y' &&
			a[i] != 'A' && a[i] != 'E' && a[i] != 'O' && a[i] != 'U' && a[i] != 'I' && a[i] != 'Y')
		{
			if (a[i] >= 65 && a[i] <= 92)
			{
				a[i] = a[i] + 32;
				cout <<'.'<< a[i];
			}
			else
				cout << '.' << a[i];

		}

	}
	
}