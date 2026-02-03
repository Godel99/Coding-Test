#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using pll = pair<ll, ll>;
const int dy[]={-1,0,1,0},dx[]={0,1,0,-1};

char board[25][25];
ld d[25][25];

ld solve(){
	int n, m, sy, sx, t; cin >> n >> m >> sy >> sx >> t; sy++; sx++;
	ld p, q; cin >> p >> q;
	for(int i = 1; i <= n; i++) for(int j = 1; j <= m; j++){
		cin >> board[i][j];
		if(board[i][j] == 'A') d[i][j] = p;
		else d[i][j] = q;
	}
	ld ans = 0;
	for(int path = 0; path < (1<<(2*t)); path++){
		int y = sy, x = sx; ld tmp = 0; bool ok = 1;
		for(int i = 0; i < t; i++){
			int k = (path>>(i*2))&3;
			y += dy[k]; x += dx[k];
			if(y < 1 || y > n || x < 1 || x > m){
				ok = 0; continue;
			}
			tmp += d[y][x];
			if(board[y][x] == 'A') d[y][x] *= 1-p;
			else d[y][x] *= 1-q;
		}
		if(ok) ans = max(ans, tmp);
		y = sy; x = sx;
		for(int i = 0; i < t; i++){
			int k = (path>>(i*2))&3;
			y += dy[k]; x += dx[k];
			if(y < 1 || y > n || x < 1 || x > m) continue;
			if(board[y][x] == 'A') d[y][x] = p;
			else d[y][x] = q;
		}
	}
	return ans;
}

int main(){
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	int T; cin >> T; cout << fixed << setprecision(12);
	for(int tc = 1; tc <= T; tc++) cout << "Case #" << tc << ": " << solve() << '\n';
}