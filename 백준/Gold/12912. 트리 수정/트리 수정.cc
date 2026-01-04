#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

int N;
vector<vector<pll>> graph;
vector<tuple<int, int, int>> edges;

pll DFS(int start, int pre, int blocked_edge){
    vector<bool> visited(N, false);
    stack<pll> st;

    st.push({start, 0});
    visited[start] = true;

    int node = start;
    ll max_dist = 0;

    while (!st.empty()){
        auto [cur, dist] = st.top(); st.pop();

        if (dist > max_dist){
            max_dist = dist;
            node = cur;
        }

        for (auto [nxt, w] : graph[cur]) {
            if (nxt == pre) continue;
            if (nxt == blocked_edge) continue;
            if (!visited[nxt]){
                visited[nxt] = true;
                st.push({nxt, dist + w});
            }
        }
    }
    return {node, max_dist};
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> N;
    graph.resize(N);

    for (int i = 0; i < N-1; i++){
        int u, v; ll w;
        cin >> u >> v >> w;
        edges.push_back({u,v,w});
        graph[u].push_back({v,w});
        graph[v].push_back({u,w});
    }

    ll answer = 0;

    for (auto [u,v,w] : edges){
        answer = max(answer, DFS(DFS(u,v,v).first, v, v).second + w + DFS(DFS(v,u,u).first, u,u).second);
    }

    cout << answer;

}
