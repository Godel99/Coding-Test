#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int n, m;
vector<int> ans, a;
vector<bool> visited;

void dfs(int x, int d){
    if(d == m){
        for(int i = 0; i < ans.size(); i++) cout << ans[i] << ' ';
        cout << '\n';
        return;
    }
    for(int i = 0; i < n; i++){
        if(!visited[i]){
            visited[i] = 1;
            ans.push_back(a[i]);
            dfs(i, d+1);
            ans.pop_back();
            visited[i] = 0;
        } 
    }
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> n >> m;
    a.resize(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    visited.assign(n, 0);
    dfs(0, 0);
    return 0;
}