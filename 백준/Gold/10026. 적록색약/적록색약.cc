#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<vector<char>> board(n, vector<char>(n));
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) cin >> board[i][j];
    vector<vector<bool>> visited(n, vector<bool>(n, 0));
    int cnt1, cnt2; cnt1 = cnt2 = 0;
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++){
        if(!visited[i][j]){
            char c = board[i][j];
            queue<pii> dq; dq.push({i, j});
            visited[i][j] = 1;
            while(dq.size()){
                auto [x, y] = dq.front(); dq.pop();
                for(int dir = 0; dir < 4; dir++){
                    int nx = x+dx[dir], ny = y+dy[dir];
                    if(0 > nx || nx >= n || 0 > ny || ny >=n) continue;
                    if(board[nx][ny] == c && !visited[nx][ny]){
                        visited[nx][ny] = 1;
                        dq.push({nx, ny});
                    }
                }
            }
            cnt1++;
        }
    }
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++){
        if(board[i][j] == 'G') board[i][j] = 'R';
        visited[i][j] = 0;
    }
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++){
        if(!visited[i][j]){
            char c = board[i][j];
            queue<pii> dq; dq.push({i, j});
            visited[i][j] = 1;
            while(dq.size()){
                auto [x, y] = dq.front(); dq.pop();
                for(int dir = 0; dir < 4; dir++){
                    int nx = x+dx[dir], ny = y+dy[dir];
                    if(0 > nx || nx >= n || 0 > ny || ny >=n) continue;
                    if(board[nx][ny] == c && !visited[nx][ny]){
                        visited[nx][ny] = 1;
                        dq.push({nx, ny});
                    }
                }
            }
            cnt2++;
        }
    }
    cout << cnt1 << ' ' << cnt2;
    return 0;
}