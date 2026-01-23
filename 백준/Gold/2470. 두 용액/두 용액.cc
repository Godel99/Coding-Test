#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    ll minv = LLONG_MAX;
    vector<ll> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    int l = 0, r = n-1;
    pll ans;
    while(l < r){
        ll val = abs(a[l]+a[r]);
        if(minv > val){
            minv = val;
            ans = {a[l], a[r]};
            if(!minv) break;
        }
        if(a[l] + a[r] < 0) l++;
        else r--;
    }
    cout << ans.first << ' ' << ans.second;
	return 0;
}