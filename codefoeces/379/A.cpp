
#include <iostream>
using namespace std;
int main()
{
	int n,t,b;
	n = 0;
	int tem,total;
	
	cin >> n >> t;
	tem = n;
	total = n;
	while (tem>=t)
	{
		b = tem % t;
		tem = tem / t;
			
		total+=tem;
		tem = tem + b;
	}
	cout << total << endl;
	return 0;
}