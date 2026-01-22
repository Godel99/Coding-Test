#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<string> ans(n);
    for(int i = 0; i < n; i++) cin >> ans[i];
    sort(ans.begin(), ans.end(), [](const string& a, string& b){
        if(a.length() != b.length()) return a.length() < b.length();
        return a < b;
    });
    ans.erase(unique(ans.begin(), ans.end()), ans.end());
    for(const auto& s: ans) cout << s << '\n';
	return 0;
}