#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
using namespace std;

int n, sz, x, y, cnt;
int board[1 << 7][1 << 7];

void f(int sx, int sy, int s, int cx, int cy) { //[sx, sx + s), [sy, sy + s)범위를 칠하는데 (cx, cy)는 빈공간인 경우
	if (s == 2) {
		cnt++;
		for (int i = sx; i < sx + s; i++) for (int j = sy; j < sy + s; j++) {
			if (i == cx && j == cy) continue;
			board[i][j] = cnt;
		}
		return;
	}
	s >>= 1;
	bool flag1 = cx < sx + s;
	bool flag2 = cy < sy + s;
	if (flag1 && flag2) {
		f(sx, sy + s, s, sx + s - 1, sy + s); //UR
		f(sx + s, sy, s, sx + s, sy + s - 1); //DL
		f(sx + s, sy + s, s, sx + s, sy + s); //DR
		board[sx + s - 1][sy + s] = board[sx + s][sy + s - 1] = board[sx + s][sy + s] = ++cnt;
		f(sx, sy, s, cx, cy);
	}
	else if (flag1) {
		f(sx, sy, s, sx + s - 1, sy + s - 1); //UL
		f(sx + s, sy, s, sx + s, sy + s - 1); //DL
		f(sx + s, sy + s, s, sx + s, sy + s); //DR
		board[sx + s - 1][sy + s - 1] = board[sx + s][sy + s - 1] = board[sx + s][sy + s] = ++cnt;
		f(sx, sy + s, s, cx, cy);
	}
	else if (flag2) {
		f(sx, sy, s, sx + s - 1, sy + s - 1); //UL
		f(sx, sy + s, s, sx + s - 1, sy + s); //UR
		f(sx + s, sy + s, s, sx + s, sy + s); //DR
		board[sx + s - 1][sy + s - 1] = board[sx + s - 1][sy + s] = board[sx + s][sy + s] = ++cnt;
		f(sx + s, sy, s, cx, cy);
	}
	else {
		f(sx, sy, s, sx + s - 1, sy + s - 1); //UL
		f(sx, sy + s, s, sx + s - 1, sy + s); //UR
		f(sx + s, sy, s, sx + s, sy + s - 1); //DL
		board[sx + s - 1][sy + s - 1] = board[sx + s][sy + s - 1] = board[sx + s - 1][sy + s] = ++cnt;
		f(sx + s, sy + s, s, cx, cy);
	}
}


int main() {
	fastio;
	cin >> n >> y >> x;
	--x, --y; sz = 1 << n; x = sz - 1 - x;
	board[x][y] = -1;
	f(0, 0, sz, x, y);
	for (int i = 0; i < sz; i++) {
		for (int j = 0; j < sz; j++) cout << board[i][j] << ' ';
		cout << '\n';
	}
}