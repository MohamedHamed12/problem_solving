#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a;
    cin >> a;

    int contiguous = 1;
    for (size_t i = 1; i < a.length(); ++i)
    {
        if (a[i] == a[i - 1])
        {
            contiguous += 1;
            if (contiguous == 7)
            {
                cout << "YES" << endl;
                return 0;
            }
        }
        else
        {
            contiguous = 1;
        }
    }

    cout << "NO" << endl;
    return 0;
}