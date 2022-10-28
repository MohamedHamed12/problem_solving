
#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n,a;
	
	
	cin >> a >>n;
	while (n--)
	{
		

			if ( a%10==0)
			{
				a=a/10;
			}

			else
			{
				a--;
			}
		
	}
	cout << a << endl;
	return 0;
}