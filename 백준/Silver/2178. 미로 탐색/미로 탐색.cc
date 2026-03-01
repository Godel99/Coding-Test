#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(m));
    for(int i = 0; i < n; i++){
        string s; cin >> s;
        for(int j = 0; j < m; j++) board[i][j] = s[j]-'0';
    }
    queue<pii> q; q.push({0, 0});
    while(q.size()){
        auto [x, y] = q.front(); q.pop();
        for(int dir = 0; dir < 4; dir++){
            int nx = x+dx[dir], ny = y+dy[dir];
            if(nx >= 0 && ny >= 0 && nx < n && ny < m && board[nx][ny] == 1){
                board[nx][ny] = board[x][y]+1;
                q.push({nx, ny});
            }
        }
    }
    cout << board[n-1][m-1];
    return 0;
}