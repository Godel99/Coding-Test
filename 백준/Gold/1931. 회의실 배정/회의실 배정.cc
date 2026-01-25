#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<pll> I(n);
    for(int i = 0; i < n; i++) cin >> I[i].first >> I[i].second;
    sort(I.begin(), I.end(), [](const pll& a, const pll& b){
        if(a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });
    ll ans = 1, end = I[0].second;
    for(int i = 1; i < n; i++){
        auto[s, e] = I[i];
        if(s >= end){
            ans++; 
            end = e;
        }
    }
    cout << ans;
	return 0;
}