#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;
const ll inf = 2e18;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<pll> a(n);
    for(int i = 0; i < n; i++) cin >> a[i].first >> a[i].second;
    sort(a.begin(), a.end());
    ll L = inf, R = 0, pre = 0;
    for(int i = 0; i < n; i++){
        ll pres = pre+a[i].second;
        L = min(L, pre-a[i].first);
        R = max(R, pres-a[i].first-L);
        pre = pres;
    }
    cout << R;
    return 0;
}