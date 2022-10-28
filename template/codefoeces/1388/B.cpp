#include<bits/stdc++.h>
using namespace std;

void solve(){
    int n ;
    cin >> n ;
    int temp = ceil((double)n/4) ;
    cout <<string(n-temp,'9') + string(temp,'8') << endl ; 
}

int main(){
    ios_base::sync_with_stdio(false);

    int testcase ;
    cin >> testcase ;
    for(int i = 0 ; i < testcase ; i ++){
        solve();
    }

    return 0 ;
}