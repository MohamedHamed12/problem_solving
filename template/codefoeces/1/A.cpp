#include <iostream>
#include "string"
using namespace std;
int n, m, a;
long long x, y;
int main() {
	cin >> n >> m >> a;
	x = n / a;
	y = m / a;
	if (n % a != 0) {
		x = x + 1;
	}
	if (m % a != 0) {
		y = y + 1;
	}

	cout << x*y;
}