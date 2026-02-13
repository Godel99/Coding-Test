#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    unordered_set<string> us; string name; 
    for(int i = 0; i < n; i++){
        cin >> name;
        us.insert(name);
    }
    vector<string> ans;
    for(int i = 0; i < m; i++){
        cin >> name;
        if(us.find(name) != us.end()) ans.push_back(name);
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for(auto& name: ans) cout << name << '\n';
    return 0;
}