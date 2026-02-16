#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> score(n+1, 0), dp(n+1, 0);
    for(int i = 1; i <= n; i++) cin >> score[i];
    if(n == 1) return !(cout << score[1]);
    if(n == 2) return !(cout << score[1]+score[2]);
    dp[1] = score[1];
    dp[2] = score[1]+score[2];
    dp[3] = max(score[1], score[2])+score[3];
    for(int i = 4; i <= n; i++) dp[i] = max(dp[i-3]+score[i-1], dp[i-2])+score[i];
    cout << dp[n];
    return 0;
}