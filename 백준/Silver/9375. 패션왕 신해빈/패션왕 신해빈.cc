#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        unordered_map<string, int> data;
        for(int i = 0; i < n; i++){
            string c, s; cin >> c >> s;
            data[s]++;
        }
        int ans = 1;
        for(auto& [s, cnt] : data) ans *= (cnt+1);
        cout << ans-1 << '\n';
    }
    return 0;
}