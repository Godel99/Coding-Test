#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    pii start;
    vector<vector<char>> board(n, vector<char>(m));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> board[i][j];
            if(board[i][j] == 'I'){
                board[i][j] = 'X';
                start = {i, j};
            }
        }
    }
    stack<pii> st;
    st.push(start);
    int ans = 0;
    while(st.size()){
        auto[x, y] = st.top(); st.pop();
        for(int dir = 0; dir < 4; dir++){
            int nx = x+dx[dir], ny = y+dy[dir];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(board[nx][ny] != 'X'){
                if(board[nx][ny] == 'P') ans++;
                board[nx][ny] = 'X';
                st.push({nx, ny});
            }
        }
    }
    if(ans) cout << ans;
    else cout << "TT";
    return 0;
}