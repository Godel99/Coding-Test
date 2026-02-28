#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
const int INF = 0x3f3f3f3f;
const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int n, m;
vector<vector<char>> a;

int solved(pii start, pii end, bool type){
    auto [ay, ax] = start; auto [by, bx] = end;
    vector<queue<pii>> q(3);
    vector<vector<int>> dp(n, vector<int>(n, INF));
    q[0].push(start);
    dp[ay][ax] = 0;
    int res = 0;
    while(q[0].size() || q[1].size() || q[2].size()){
        while(q[res%3].empty()) res++;
        while(q[res%3].size()){
            auto [y, x] = q[res%3].front(); q[res%3].pop();
            if(dp[y][x] < res) continue;
            for(int dir = 0; dir < 4; dir++){
                int ny = y+dy[dir], nx = x+dx[dir];
                if(ny < 0 || nx < 0 || ny >= n || nx >= n) continue;
                int nd = dp[y][x]+(a[ny][nx] == "ab"[type^(res&1)]);
                if(a[ny][nx] == "ba"[type] && !res) nd = 2;
                if(dp[ny][nx] <= nd) continue; dp[ny][nx] = nd; q[nd%3].push({ny, nx});
            }
        }
    }
    if(dp[by][bx] > 1) return INF;
    return res;
}

int main(){
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> n >> m;
    a.assign(n, vector<char>(n, ' '));
    pii start, end; start = end = {};
    bool isa, isb; isa = isb = 0;
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++){
        cin >> a[i][j];
        if(a[i][j] == 'A') start = {i, j};
        if(a[i][j] == 'B') end = {i, j};
        if(a[i][j] == 'a') isa = 1;
        if(a[i][j] == 'b') isb = 1;
    }
    if(!isa && !isb){cout << 0; return 0;}
    if(!isa || !isb){cout << 1; return 0;}
    int ans = INF; ans = min(ans, solved(start, end, 0)); ans = min(ans, solved(end, start, 1));
    if(ans == INF) cout << -1;
    else cout << ans;
	return 0;
}