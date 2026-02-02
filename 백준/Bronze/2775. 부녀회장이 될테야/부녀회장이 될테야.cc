#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int dp[15];

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int k, n; cin >> k >> n;
        for(int i = 1; i <= n; i++) dp[i] = i;
        for(int i = 1; i <= k; i++){
            for(int j = 2; j <= n; j++) dp[j] += dp[j-1];
        }
        cout << dp[n] << '\n';
    }
    return 0;
}