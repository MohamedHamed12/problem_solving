#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
const int mod = 1e9+7;
const int maxn = 40010;
long long a[maxn];
long long b[maxn] = {0};
long long dp[maxn][550] = {0};
long long ans[maxn];

long long check(long long x){
	string s = "";
	while(x){
		s += char(x%10+'a');
		x /= 10;
	}
	string s1 = s;
	reverse(s.begin(), s.end());
	if(s == s1) return 1;
	else return 0;
}

int main(){
	long long t;
	cin >> t;
	//pre 
	long long cnt = 0; 
	for(long long i = 0;i <= 40000;i++){
		if(check(i)){
			a[cnt++] = i;
			b[i] = 1;
			//cout << i << " ";
		}
	}
	//cout << cnt << endl;//498
	dp[0][0] = 1;
	dp[1][0] = 0;
	dp[1][1] = 1;
	ans[0] = ans[1] = 1;
	for(long long i = 2;i<40001;i++){
		long long jj = 0;
		for(long long j = 1;j<cnt&&a[j]*2 <= i;j++){
			dp[i][j] = (dp[i][j-1]+ans[i-a[j]]-dp[i-a[j]][j-1]+mod)%mod;
			//cout << a[j] << " " << i-a[j] << " " << dp[i-a[j]][j-1] << " " << dp[i][j] << endl;
			ans[i] = dp[i][j];
			jj = j;
		}
		for(long long j = jj+1;a[j]<i&&j<cnt;j++){//a[j]<i&&j<cnt 
			dp[i][j] = dp[i][jj]%mod;
		}
		if(b[i] == 1){
			dp[i][i] = ans[i]+1;
			ans[i] = dp[i][i]%mod;
		}
		//cout << ans[i] << endl;
		//if(i == 7) break;
	}
	while(t--){
		long long n;
	    cin >> n;
        cout << (ans[n]+mod)%mod << endl;
	}
	return 0;
}