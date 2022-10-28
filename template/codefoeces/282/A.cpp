
#include <iostream>
#include "string"
using namespace std;
int main()
{
	int n, X;
	cin >> n;
	X = 0;
	string op;
	while (n--)
	{
		cin >> op;
		if (op == "X++" || op == "++X")
		{
			X += 1;
		}
		if (op == "X--" || op == "--X")
		{
			X = X - 1;

		}
	}
	cout << X << endl;
}