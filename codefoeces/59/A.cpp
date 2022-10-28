
#include <iostream>
#include "string"
#include <cctype>
#include <cctype>

using namespace std;
int main()
{
	string a;
	int n=0;
	cin >> a;
	for (int i = 0; i < a.length() ; i++)
	{
		if (isupper(a[i]))
		{
			n += 1;
		}

	}
	
	if (n > .5* a.length())
	{
		for (int i = 0; i < a.length(); i++)
		{
			a[i] = toupper(a[i]);

		}
		
	}
	else
	{
		for (int i = 0; i < a.length(); i++)
		{
			a[i] =tolower(a[i]);
		
		}

	}
	cout << a << endl;

}