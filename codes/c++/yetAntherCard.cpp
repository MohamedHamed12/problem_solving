// #include <iostream>
// using namespace std;
// int main (){
//     int a,b;
//     cin>>a>>b;
//     int l1[1000];
//     int l2[1000];
//     for (int i = 0; i < a; i++)
//     {
//         cin>>l1[i];
//     }
//     for (int i = 0; i < b; i++)
//     {
//         cin>>l2[i];
//     }
//     for (int i = 0; i < b; i++)
//     {
//         for
//     }
    
    



// }
// #include <iostream>
// using namespace std;
// int n, q, a[300005];
// bool vis[55];
// void move(int pos) {
// 	int tmp = a[pos];
// 	for(int i = pos - 1; i >= 1; i--) a[i + 1] = a[i];
// 	a[1] = tmp;
// }
// int main() {
// 	ios::sync_with_stdio(false);
// 	memset(vis, 0, sizeof(vis));
// 	cin >> n >> q;
// 	for(int i = 1; i <= n; i++) cin >> a[i];
// 	for(int i = 1; i <= q; i++) {
// 		int nq;
// 		cin >> nq;
// 		int pos = 0;
// 		for(int i = 1; i <= n; i++) {
// 			if(a[i] == nq) {
// 				pos = i;
// 				break;
// 			}
// 		}
// 		cout << pos << ' ';
// 		move(pos);
// 	}
// 	return 0;
// }
#include <string>
#include <array>

#include <iostream>
using namespace std;
int main(){


string a[3][3];
  a[0][0]="mm";
  a[0][1]="ne";
  a[1][1]="fs";
  a[1][0]="mms";

int rows =  sizeof a / sizeof a[0][0];  
cout<<rows<<endl;

  
  
    return 0;
}
// #include <iostream>
// using namespace std;
// template<typename t,typename t2>
// t2 sswap (t & a,t & b)
// {
//     t tem=a;
//     a=b;
//     b=tem;
//     return tem*2;

// }
// int main(){
// int a,b;
//    cin>>a>>b;
//    int m =sswap<int,int>(a,b);
//    cout<<a<<b<<m;
//     return 0;
// }