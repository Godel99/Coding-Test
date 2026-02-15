#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<pii> dp(n+2);
        dp[0] = {1, 0}, dp[1] = {0, 1};
        for(int i = 2; i < n+2; i++){
            dp[i].first = dp[i-1].first+dp[i-2].first;
            dp[i].second = dp[i-1].second+dp[i-2].second;
        }
        cout << dp[n].first << ' ' << dp[n].second << '\n';
    }
    return 0;
}