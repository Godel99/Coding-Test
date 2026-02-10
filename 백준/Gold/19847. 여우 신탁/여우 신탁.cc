#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, now; cin >> n >> now;
    int tot = now;
    vector<int> dp(now, 1);
    for(int i = 1; i < n; i++){
        int x; cin >> x;
        while(now > x){ 
            dp[now-1-x] += dp[now-1];
            now--;
        }
    }
    ll ans = 0;
    for(int i = 1; i < now; i++) ans+= i*dp[i];
    cout << setprecision(12) << fixed << double(ans) / tot;
    return 0;
}