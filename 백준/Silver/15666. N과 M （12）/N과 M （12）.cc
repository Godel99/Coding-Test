#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int n, m;
vector<int> ans, a;

void dfs(int x){
    if(ans.size() == m){
        for(int i = 0; i < ans.size(); i++) cout << ans[i] << ' ';
        cout << '\n';
        return;
    }
    for(int i = x; i < a.size(); i++){
        ans.push_back(a[i]);
        dfs(i);
        ans.pop_back();
    }
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> n >> m;
    unordered_set<int> s;
    for(int i = 0; i < n; i++){
        int x; cin >> x;
        s.insert(x);
    }
    for(auto x : s) a.push_back(x);
    sort(a.begin(), a.end());
    dfs(0);
    return 0;
}