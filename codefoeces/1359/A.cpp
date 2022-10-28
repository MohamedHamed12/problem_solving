
#include <iostream>
using namespace std;
int main()
{
    int t;
	int n, m, k;
	
	float x,o;
	float y = 0;
    cin >> t;

	while (t--)
	{

		cin >>  n>> m >> k;
		x = n / k;
		if (m==0)
		{
			cout << 0 << endl;
			
		}

		
		else if (m<=x)
		{
			cout << m<< endl;
			
		}
		else
		{
			
			y = ((m-x)/(k - 1));
			y=ceil(y);
			
			cout << x - y << endl;
		
		}
	}
	return 0;
}