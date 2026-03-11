#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int n, m;
vector<int> ans;

void dfs(int x, int d){
    if(d == m){
        for(int i = 0; i < ans.size(); i++) cout << ans[i] << ' ';
        cout << '\n';
        return;
    }
    for(int i = x; i <= n; i++){
        ans.push_back(i);
        dfs(i+1, d+1);
        ans.pop_back();
    }
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> n >> m;
    dfs(1, 0);
    return 0;
}