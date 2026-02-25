#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<int>> edge(n+1);
    vector<bool> visited(n+1, false);
    for(int i = 0; i < m; i++){
        int x, y; cin >> x >> y;
        edge[x].push_back(y);
        edge[y].push_back(x);
    }
    int ans = 0;
    for(int i = 1; i <= n; i++){
        if(!visited[i]){
            visited[i] = true;
            stack<int> st;
            st.push(i);
            ans++;
            while(st.size()){
                int cur = st.top(); st.pop();
                for(auto nxt : edge[cur]){
                    if(!visited[nxt]){
                        visited[nxt] = true;
                        st.push(nxt);
                    }
                }
            }
        }
    }
    cout << ans;
    return 0;
}