#include<bits/stdc++.h>
#define ll long long int
using namespace std;
const int N = 300;
ll dp[N+1][N+1];
 
ll update(int n , int a , int b , int w){
	
	dp[a][b] = dp[b][a] = min(dp[a][b] , w*1LL);
	ll result = 0;
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			dp[i][j] = min(dp[i][j] , dp[i][a] + dp[a][b] + dp[b][j]);
			dp[i][j] = min(dp[i][j] , dp[i][b] + dp[b][a] + dp[a][j]);
			result += dp[i][j];
		}
	}
	return result/2;
}
 
int main(){
	int n , k , a , b , w;
	
	cin>>n;
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++) cin>>dp[i][j];
	}
	
	cin>>k;
	while(k--){
		cin>>a>>b>>w;
		cout<<update(n , a , b , w)<<" ";
	}
}