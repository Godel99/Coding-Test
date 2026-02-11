#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, q, idx; cin >> n >> q; idx = n;
    vector<int> a(n+q+1, 0);
    ll cnt[32] = {}, e = 0;
    for(int i = 1; i <= n; i++){
        cin >> a[i];
        for(int bit = 0; bit < 32; bit++) if(a[i]&(1<<bit)) cnt[bit]++;
    }
    while(q--){
        int query; cin >> query;
        if(query == 1){
            int v; cin >> v; a[++idx] = v^e; n++;
            for(int bit = 0; bit < 32; bit++) if(a[idx]&(1<<bit)) cnt[bit]++;
        }
        else if(query == 2){
            int p; cin >> p; n--;
            for(int bit = 0; bit < 32; bit++) if(a[p]&(1<<bit)) cnt[bit]--;
        }
        else {
            int t; cin >> t; e ^= t;
        }
        ll ans = 0;
        for(int bit = 0; bit < 32; bit++){
            if(e&(1LL<<bit)) ans += (n-cnt[bit])<<bit;
            else ans += cnt[bit]<<bit;
        }
        cout << ans << '\n';
    }
    return 0;
}