#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

#define X first
#define Y second

const int INF = int(1e9);

string board[1000];
int dist1[1000][1000];
int dist2[1000][1000];
int n, m;

int main() {
	fastio;
	cin >> n >> m;
	for (int i = 0; i < n; i++) cin >> board[i];

	queue<pair<int, int>> Q;
	Q.push({ 0, 0 });
	dist1[0][0] = 1;
	while (!Q.empty()) {
		auto cur = Q.front(); Q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = cur.X + "2101"[i] - '1';
			int ny = cur.Y + "1012"[i] - '1';
			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if (board[nx][ny] == '1' || dist1[nx][ny] != 0) continue;
			Q.push({ nx, ny });
			dist1[nx][ny] = dist1[cur.X][cur.Y] + 1;
		}
	}

	Q.push({ n - 1, m - 1 });
	dist2[n - 1][m - 1] = 1;
	while (!Q.empty()) {
		auto cur = Q.front(); Q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = cur.X + "2101"[i] - '1';
			int ny = cur.Y + "1012"[i] - '1';
			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if (board[nx][ny] == '1' || dist2[nx][ny] != 0) continue;
			Q.push({ nx, ny });
			dist2[nx][ny] = dist2[cur.X][cur.Y] + 1;
		}
	}

	int mx = INF;
	if (dist1[n - 1][m - 1] != 0) mx = dist1[n - 1][m - 1];
	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
		if (board[i][j] == '0') continue;
		int mx1 = INF, mx2 = INF;
		for (int k = 0; k < 4; k++) {
			int nx = i + "2101"[k] - '1';
			int ny = j + "1012"[k] - '1';
			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if (dist1[nx][ny] > 0) mx1 = min(mx1, dist1[nx][ny]);
			if (dist2[nx][ny] > 0) mx2 = min(mx2, dist2[nx][ny]);
		}
		mx = min(mx, mx1 + mx2 + 1);
	}
	if (mx != INF) cout << mx << '\n';
	else cout << -1 << '\n';
}