#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
const int INF = 0x3f3f3f3f;

int main(){
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, e, k; cin >> n >> e >> k;
	vector<vector<pii>> g(n+1);
	vector<queue<int>> q(11);
	vector<int> dp(n+1, INF);
	for(int i = 0; i < e; i++){
		int u, v, w; cin >> u >> v >> w;
		g[u].push_back({v, w});
	}
	dp[k] = 0;
	q[1].push(k);
	int cnt, h; cnt = h = 1;
	while(cnt){
		while(q[h%11].empty()) h++;
		while(q[h%11].size()){
			int cur = q[h%11].front(); q[h%11].pop(); cnt--;
			for(auto [nxt, w] : g[cur]){
				if(dp[nxt] > dp[cur]+w){
					dp[nxt] = dp[cur]+w;
					q[dp[nxt]%11].push(nxt);
					cnt++;
				}
			}
		}
	}
	for(int i = 1; i <= n; i++){
		if(dp[i] == INF) cout << "INF\n";
		else cout << dp[i] << '\n';
	}
	return 0;
}