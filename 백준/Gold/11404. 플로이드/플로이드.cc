#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int inf = 0x3f3f3f3f;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<int>> dp(n+1, vector<int>(n+1, inf));
    for(int i = 1; i <= n; i++) dp[i][i] = 0;
    for(int i = 0; i < m; i++){
        int u, v, w; cin >> u >> v >> w;
        dp[u][v] = min(dp[u][v], w);
    }
    for(int k = 1; k <= n; k++) for(int i = 1; i <= n; i++) for(int j = 1; j <= n; j++) dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]);
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if(dp[i][j] == inf) cout << 0 << ' ';
            else cout << dp[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}