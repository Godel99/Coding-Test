#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(m));
    vector<vector<bool>> visited(n, vector<bool>(m, 0));
    pii start = {};
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++){
        cin >> board[i][j];
        if(board[i][j] == 2){
            start = {i, j};
            board[i][j] = 0;
            visited[i][j] = 1;
        }
    }
    queue<pii> q; q.push(start);
    while(q.size()){
        auto [x, y] = q.front(); q.pop();
        for(int dir = 0; dir < 4; dir++){
            int nx = x+dx[dir], ny = y+dy[dir];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(board[nx][ny] == 1 && !visited[nx][ny]){
                visited[nx][ny] = 1;
                board[nx][ny] = board[x][y]+1;
                q.push({nx, ny});
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(board[i][j] && !visited[i][j]) cout << -1 << ' ';
            else cout << board[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}