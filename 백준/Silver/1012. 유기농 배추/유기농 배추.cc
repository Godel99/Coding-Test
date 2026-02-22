#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int m, n, k; cin >> m >> n >> k;
        vector<vector<int>> board(n, vector<int>(m, 0));
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        int cnt = 0;
        for(int i = 0; i < k; i++){
            int x, y; cin >> x >> y;
            board[y][x] = 1;
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(board[i][j] && !visited[i][j]){
                    cnt++;
                    visited[i][j] = true;
                    stack<pii> st;
                    st.push({i, j});
                    while(st.size()){
                        auto [x, y] = st.top(); st.pop();
                        for(int dir = 0; dir < 4; dir++){
                            int nx = x+dx[dir], ny = y+dy[dir];
                            if(0 <= nx && nx < n && 0 <= ny && ny < m){
                                if(board[nx][ny] && !visited[nx][ny]){
                                    visited[nx][ny] = true;
                                    st.push({nx, ny});
                                }
                            }
                        }
                    }
                }
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}