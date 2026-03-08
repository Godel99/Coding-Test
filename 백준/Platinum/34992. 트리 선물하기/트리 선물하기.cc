#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int k; cin >> k;
    vector<int> s(k+1);
    for(int i = 1; i <= k; i++) cin >> s[i];
    if(s[1] != 0){cout << -1; return 0;}
    int n = s[k];
    vector<int> par(n/2+1, 0);
    vector<pii> tree(n+1, {0, 0});
    cout << n/2 << '\n';
    for(int i = 1; i <= n; i += 2) par[i/2+1] = i;
    int idx = 2;
    for(int i = 1; i < n/2; i++){
        if(s[idx] != i*2) swap(par[i], par[i+1]);
        else idx++;
    }
    for(int i = 1; i <= n/2; i++) tree[par[i]] = {par[i-1], i*2};
    for(int i = 1; i <= n; i += 2) cout << tree[i].first << ' ' << tree[i].second << '\n';
    return 0;
}