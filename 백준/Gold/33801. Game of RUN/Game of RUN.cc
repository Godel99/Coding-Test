#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 1'000'000'007;

ll dp[1000001][5];

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    dp[1][0] = 1;
    dp[2][0] = 3;
    dp[2][1] = dp[2][2] = dp[2][3] = dp[2][4] = 1;
    for(int i = 3; i <= 1000000; i++){
        dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2]+dp[i-1][3]+dp[i-1][4])%MOD;
        dp[i][1] = (dp[i-1][0]+dp[i-1][1])%MOD;
        dp[i][2] = (dp[i-1][0]+dp[i-1][2])%MOD;
        dp[i][3] = (dp[i-1][2]+dp[i-1][3])%MOD;
        dp[i][4] = (dp[i-1][1]+dp[i-1][4])%MOD;
    }
    int T; cin >> T;
    for(int i = 0; i < T; i++){
        int n; cin >> n; cout << (dp[n][0]+dp[n][1]+dp[n][2])%MOD << '\n';
    }
    return 0;
}