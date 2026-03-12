#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int v, d; cin >> v >> d;
        vector<int> a(v+1, 0);
        int s = 0;
        for(int i = 1; i <= v; i++){
            cin >> a[i];
            s += a[i];
        }
        if(s <= d){cout << 1 << '\n'; continue;}
        sort(a.begin(), a.end());
        if(a[1] > d){cout << 0 << '\n'; continue;}
        vector<int> pref(v+1, 0);
        for(int i = 1; i <= v; i++) pref[i] = pref[i-1]+a[i];
        vector<ll> dp(d+1, 0);
        dp[0] = 1;
        ll ans = 0;
        for(int i = v; i > 0; i--){
            int r = d-pref[i-1];
            if(r >= 0) for(int j = r; j > max(-1, r-a[i]); j--) ans += dp[j];
            for(int j = d; j >= a[i]; j--) dp[j] += dp[j-a[i]];
        }
        cout << ans << '\n';
    }
    return 0;
}