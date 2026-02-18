#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<int>> e(n+1);
    for(int i = 0; i < m; i++){
        int x, y; cin >> x >> y;
        e[x].push_back(y);
        e[y].push_back(x);
    }
    stack<int> st; st.push(1);
    vector<bool> visited(n+1, false); visited[1] = true;
    int ans = 0;
    while(st.size()){
        int cur = st.top(); st.pop();
        for(auto nxt : e[cur]){
            if(!visited[nxt]){
                visited[nxt] = true;
                ans++;
                st.push(nxt);
            }
        }
    }
    cout << ans;
    return 0;
}