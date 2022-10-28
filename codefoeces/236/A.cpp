

#include <iostream>
#include "string"
#include <algorithm>

using namespace std;

int main()
{
	

	
	
	
	
    string a;
	cin >> a;


	
	sort(a.begin(),a.end());
	a.erase(unique(a.begin(), a.end()), a.end());
	
	if (a.length() % 2 == 0)
	{
		cout << "CHAT WITH HER!" << endl;
	}
	else
	{
		cout << "IGNORE HIM!" << endl;
	}
	return 0;
}