#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    priority_queue<ll, vector<ll>, greater<ll>> min_hq;
    for(int i = 0; i < n; i++){
        ll m; cin >> m;
        min_hq.push(m);
    }
    ll ans = 0;
    while(min_hq.size() > 1){
        ll a = min_hq.top(); min_hq.pop();
        ll b = min_hq.top(); min_hq.pop();
        ans += a+b;
        min_hq.push(a+b);
    }
    cout << ans;
    return 0;
}