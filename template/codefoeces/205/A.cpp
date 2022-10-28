
#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n,min,b,t;
	t = 0;
	b = 0;
	long long a [100000] ;
	cin >> n;
	cin >> a[0];
	min = a[0];
	for (int i = 1; i < n; i++)
	{
		cin >> a[i];
		if (min > a[i])
		{
			min = a[i];
			t = i;
			b = 0;
		}
		else if (min == a[i])
		{
			b = 1;
		}
		else
		{
			continue;
		}
	}
	
	if(b==0)
	{
		cout << t + 1 << endl;
		return 0;
	}
	if (b == 1)
	{
		cout << "Still Rozdil"<< endl;
		return 0;
	}
		
	
}