
#include <iostream>
using namespace std;
int main()
{
    long long n, m,house,piont,count;
    piont = 1;
    count = 0;
    cin >> n >> m;
    for (int i = 0; i < m;i++) 
    {
      
        cin >> house;
        if (house <piont )
        {
            count += (n - piont) + (house );
        }
        else
        {
            count += (house - piont);
        }
        
        piont = house;
    }
    cout << count << endl;
    return 0;
}