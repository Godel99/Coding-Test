#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int m, n; cin >> m >> n;
    vector<vector<int>> tomato(n, vector<int>(m));
    queue<pii> q;
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++){
        cin >> tomato[i][j];
        if(tomato[i][j] == 1) q.push({i, j});
    }
    while(q.size()){
        auto [x, y] = q.front(); q.pop();
        for(int dir = 0; dir < 4; dir++){
            int nx = x+dx[dir], ny = y+dy[dir];
            if(0 > nx || nx >= n || 0 > ny || ny >= m) continue;
            if(tomato[nx][ny] == 0){
                tomato[nx][ny] = tomato[x][y]+1;
                q.push({nx, ny});
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++){
        if(tomato[i][j] == 0){
            cout << -1;
            return 0;
        }
        ans = max(ans, tomato[i][j]);
    }
    cout << ans-1;
    return 0;
}