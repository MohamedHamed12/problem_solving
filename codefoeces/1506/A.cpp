
#include <iostream>
using namespace std;
int main()
{
	int t;
	long long x,n, m, tem,nat;
	int s, h;
	s =  0;
	
	cin >> t;
	while (t--)
	{
		nat = 0;
		s = 0;
		h = 1;
		cin >> n >> m >> x;
		s = x;
		if (x > n)
		{
			tem = x / n,
				s = x - tem * n;
			h = tem+1;
		}
	
		if (s== 0 )
		{
			s = n;
			h = h - 1;
		}
		nat = (s - 1) * m + h;
		cout << nat << endl;
	}
	return 0;
}