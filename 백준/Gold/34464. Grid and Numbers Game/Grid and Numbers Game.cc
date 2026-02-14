#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using ai3 = array<int, 3>;
const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        vector<vector<int>> d(n+2, vector<int>(m+2, -1));
        vector<ai3> v;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                int x; cin >> x;
                v.push_back({x, i, j});
            }
        }
        sort(v.begin(), v.end());
        for(auto& [x, i, j] : v){
            for(int dir = 0; dir < 4; dir++) d[i][j] = max(d[i][j], d[i+dy[dir]][j+dx[dir]]+1);
        }
        int ans = 0;
        for(auto& [x, i, j] : v) ans ^= (x-d[i][j]);
        cout << (ans&1 ? "Yes\n" : "No\n");
    }
    return 0;
}