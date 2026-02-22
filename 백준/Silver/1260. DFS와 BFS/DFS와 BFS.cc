#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void dfs(int v, vector<vector<int>>& edge, vector<bool>& visited){
    visited[v] = true;
    cout << v << ' ';
    for(auto nxt : edge[v]){
        if(!visited[nxt]) dfs(nxt, edge, visited);
    }
}

void bfs(int v, vector<vector<int>>& edge, vector<bool>& visited){
    visited[v] = true;
    queue<int> q; q.push(v);
    while(q.size()){
        int cur = q.front(); q.pop();
        cout << cur << ' ';
        for(auto nxt : edge[cur]){
            if(!visited[nxt]){
                visited[nxt] = true;
                q.push(nxt);
            }
        }
    }
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m, v; cin >> n >> m >> v;
    vector<vector<int>> edge(n+1);
    vector<bool> visited(n+1, false);
    for(int i = 0; i < m; i++){
        int x, y; cin >> x >> y;
        edge[x].push_back(y);
        edge[y].push_back(x);
    }
    for(int i = 1; i <= n; i++) sort(edge[i].begin(), edge[i].end());
    dfs(v, edge, visited);
    cout << '\n';
    fill(visited.begin(), visited.end(), false);
    bfs(v, edge, visited);
    return 0;
}