#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
const int INF = 1e9;

vector<int> dijkstra(int s, int n, vector<vector<pii>>& g){
    vector<int> dist(n+1, INF);
    dist[s] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, s});

    while(!pq.empty()){
        auto [cost, cur] = pq.top();
        pq.pop();

        if(cost > dist[cur]) continue;
        for(auto [nxt, w] : g[cur]){
            if(dist[nxt] > cost+w){
                dist[nxt] = cost+w;
                pq.push({dist[nxt], nxt});
            }
        }
    }
    return dist;
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares){
    vector<vector<pii>> graph(n+1);
    for (auto &f : fares){
        int u = f[0], v = f[1], w = f[2];
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }
    vector<int> distS = dijkstra(s, n, graph);
    vector<int> distA = dijkstra(a, n, graph);
    vector<int> distB = dijkstra(b, n, graph);
    int ans = INF;
    for(int k = 1; k <= n; k++){
        if (distS[k] == INF || distA[k] == INF || distB[k] == INF) continue;
        ans = min(ans, distS[k]+distA[k]+distB[k]);
    }
    return ans;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    return 0;
}