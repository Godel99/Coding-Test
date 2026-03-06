#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using ai3 = array<int, 3>;

const int dx[] = {0, 0, 1, -1, 0, 0}, dy[] = {0, 0, 0, 0, 1, -1}, dz[] = {1, -1, 0, 0, 0, 0};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int m, n, h; cin >> m >> n >> h;
    vector<vector<vector<int>>> tomato(h, vector<vector<int>>(n, vector<int>(m)));
    queue<ai3> q;
    for(int i = 0; i < h; i++) for(int j = 0; j < n; j++) for(int k = 0; k < m; k++){
        cin >> tomato[i][j][k];
        if(tomato[i][j][k] == 1) q.push({i, j, k});
    }
    while(q.size()){
        auto [z, y, x] = q.front(); q.pop();
        for(int dir = 0; dir < 6; dir++){
            int nz = z+dz[dir], ny = y+dy[dir], nx = x+dx[dir];
            if(0 > nz || nz >= h || 0 > ny || ny >= n || 0 > nx || nx >= m) continue;
            if(tomato[nz][ny][nx] == 0){
                tomato[nz][ny][nx] = tomato[z][y][x]+1;
                q.push({nz, ny, nx});
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < h; i++) for(int j=0; j < n; j++) for(int k = 0; k < m; k++){
        if(tomato[i][j][k] == 0){
            cout << -1;
            return 0;
        }
        ans = max(ans, tomato[i][j][k]);
    }
    cout << (ans ? ans-1 : 0);
    return 0;
}