#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int INF = 0x3f3f3f3f;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<int>> e(n+1);
    for(int i = 0; i < m; i++){
        int x, y; cin >> x >> y;
        e[x].push_back(y);
        e[y].push_back(x);
    }
    int min_d = INF;
    int ans = 0;
    for(int i = 1; i <= n; i++){
        vector<int> dist(n+1, -1);
        queue<int> q; q.push(i);
        dist[i] = 0;
        while(q.size()){
            int cur = q.front(); q.pop();
            for(auto nxt : e[cur]){
                if(dist[nxt] == -1){
                    dist[nxt] = dist[cur]+1;
                    q.push(nxt);
                }
            }
        }
        int sum_d = accumulate(dist.begin(), dist.end(), 0)+1;
        if(min_d > sum_d) min_d = sum_d, ans = i;
    }
    cout << ans;
    return 0;
}