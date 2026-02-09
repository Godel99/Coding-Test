#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int indeg[101];
ll need[101][101];

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<pii>> g(n+1);
    for(int i = 0; i < m; i++){
        int x, y, k; cin >> x >> y >> k;
        g[y].push_back({x, k});
        indeg[x]++;
    }
    queue<int> q;
    for(int i = 1; i <= n; i++){
        if(!indeg[i]){
            q.push(i);
            need[i][i] = 1;
        }
    }
    while(q.size()){
        int now = q.front(); q.pop();
        for(auto [nxt, k]: g[now]){
            for(int i = 1; i <= n; i++) need[nxt][i] +=need[now][i]*k;
            indeg[nxt]--;
            if(!indeg[nxt]) q.push(nxt);
        }
    }
    for(int i = 1; i <= n; i++) if(need[n][i]) cout << i << ' ' << need[n][i] << '\n';
    return 0;
}