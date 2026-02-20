#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> dp(n+1, 0);
    dp[1] = 1;
    dp[2] = 2;
    for(int i = 3; i <= n; i++) dp[i] = (dp[i-1]+dp[i-2])%10007;
    cout << dp[n];
    return 0;
}