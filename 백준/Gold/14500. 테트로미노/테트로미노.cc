#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
vector<vector<int>> board;
vector<vector<bool>> visited;
int n, m, ans, maxv;

void dfs(int x, int y, int d, int s){
    if(s+maxv*(4-d) <= ans) return;
    if(d == 4){ans = max(ans, s); return;}
    for(int dir = 0; dir < 4; dir++){
        int nx = x+dx[dir], ny = y+dy[dir];
        if(0 > nx || nx >= n || 0 > ny || ny >= m || visited[nx][ny]) continue;
        if(d == 2){
            visited[nx][ny] = 1;
            dfs(x, y, d+1, s+board[nx][ny]);
            visited[nx][ny] = 0;
        }
        visited[nx][ny] = 1;
        dfs(nx, ny, d+1, s+board[nx][ny]);
        visited[nx][ny] = 0;
    }
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> n >> m;
    board.assign(n, vector<int>(m));
    visited.assign(n, vector<bool>(m, 0));
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) cin >> board[i][j];
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) maxv = max(maxv, board[i][j]);
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++){
        visited[i][j] = 1;
        dfs(i, j, 1, board[i][j]);
        visited[i][j] = 0;
    }
    cout << ans;
    return 0;
}