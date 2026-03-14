#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<vector<int>> e(n+1);
    for(int i = 0; i < n-1; i++){
        int x, y; cin >> x >> y;
        e[x].push_back(y);
        e[y].push_back(x);
    }
    vector<int> par(n+1, 0);
    queue<int> q; q.push(1);
    while(q.size()){
        int cur = q.front(); q.pop();
        for(auto nxt : e[cur]){
            if(!par[nxt]){
                par[nxt] = cur;
                q.push(nxt);
            }
        }
    }
    for(int i = 2; i <= n; i++) cout << par[i] << '\n';
    return 0;
}