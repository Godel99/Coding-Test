#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, ans = 1; cin >> n;
    vector<ll> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    vector<unordered_map<ll, int>> dp(n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < i; j++){
            ll d = a[i]-a[j];
            if(dp[j].find(d)==dp[j].end()) dp[i][d] = 2;
            else dp[i][d] = dp[j][d]+1;
            ans = max(ans, dp[i][d]);  
        }
    }
    cout << ans;
    return 0;
}