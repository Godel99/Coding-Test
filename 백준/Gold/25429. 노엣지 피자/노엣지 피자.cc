#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll n, l;
unordered_map<ll, unordered_map<ll, ll>> bucket;
unordered_map<ll, ll> bucket_cnt;
unordered_map<ll, ll> mp;
int bad, q; ll sum;

void reset_tp(ll x){
    if(mp.find(x)==mp.end()) return;
    ll r = x%l;
    bucket[r][mp[x]]--;
    if(!bucket[r][mp[x]]){
        bucket_cnt[r]--;
        if(bucket_cnt[r] == 1) bad--;
        sum -= mp[x];
    }
    mp.erase(x);
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> n >> l >> q;
    while(q--){
        int op; cin >> op;
        if(op == 1){
            ll x, t, r; cin >> x >> t; 
            reset_tp(x);
            mp[x] = t;
            r = x%l;
            if(!bucket[r][t]){
                bucket_cnt[r]++;
                if(bucket_cnt[r] == 2) bad++;
                sum += t;
            }
            bucket[r][t]++;
        }
        else{
            ll x; cin >> x;
            reset_tp(x);
        }
        if(bad) cout << "NO\n";
        else cout << "YES " << sum << '\n';
    }
    return 0;
}