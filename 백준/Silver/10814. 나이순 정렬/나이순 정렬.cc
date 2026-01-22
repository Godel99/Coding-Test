#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pis = pair<int, string>;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<pis> ans(n);
    for(int i = 0; i < n; i++){
        cin >> ans[i].first >> ans[i].second;
    }
    stable_sort(ans.begin(), ans.end(), [](const pis& a, const pis& b){
        return a.first < b.first;
    });
    for(int i = 0; i < n; i++) cout << ans[i].first << ' ' << ans[i].second << '\n';
	return 0;
}