#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        if(n < 4){
            cout << 1 << '\n';
            continue;
        }
        vector<ll> dp(n+1, 0);
        dp[1] = dp[2] = dp[3] = 1;
        for(int i = 4; i <= n; i++) dp[i] = dp[i-3]+dp[i-2];
        cout << dp[n] << '\n';
    }
    return 0;
}