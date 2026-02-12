#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<pii>> e(n+1);
    vector<int> deg(n+1);
    for(int i = 1; i <= m; i++){
        int x, y; cin >> x >> y;
        e[x].push_back({y, i});
        deg[y]++;
    }
    queue<int> q;
    for(int i = 1; i <= n; i++) if(!deg[i]) q.push(i);
    int ans = 0;
    while(q.size()){
        if(q.size() > 1) return !(cout << -1);
        int cur = q.front(); q.pop();
        for(auto [nxt, idx] : e[cur]){
            deg[nxt]--;
            if(!deg[nxt]){
                q.push(nxt);
                ans = max(ans, idx);
            }
        }
    }
    cout << ans;
    return 0;
}