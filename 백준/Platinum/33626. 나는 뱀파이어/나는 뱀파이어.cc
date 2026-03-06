#include<bits/stdc++.h>
using namespace std;
using ll = long long;
vector<vector<int>> e;
int cnt, p;

int dfs(int cur, int pre, int t){
    int ret = t+1;
    for(auto nxt : e[cur]){
        if(nxt == pre) continue;
        ret = min(ret, dfs(nxt, cur, t)+1);
    }
    if(ret > t && cur != p){
        ret = 0;
        cnt++;
    }
    return ret;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m >> p;
    e.resize(n+1);
    for(int i = 1; i < n; i++){
        int u, v; cin >> u >> v;
        e[u].push_back(v);
        e[v].push_back(u);
    }
    int l = 0, r = n;
    while(l < r){
        int mid = l+r>>1;
        cnt = 0;
        dfs(p, 0, mid);
        if(cnt <= m) r = mid;
        else l = mid+1;
    }
    if(l == n) cout << -1;
    else cout << l+1;
    return 0;
}