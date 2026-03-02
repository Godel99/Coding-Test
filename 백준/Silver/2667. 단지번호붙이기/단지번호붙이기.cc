#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<vector<int>> board(n, vector<int>(n));
    for(int i = 0; i < n; i++){
        string s; cin >> s;
        for(int j = 0; j < n; j++) board[i][j] = s[j]-'0';
    }
    vector<int> ans;
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++){
        if(!board[i][j]) continue;
        board[i][j] = 0;
        int cnt = 1;
        queue<pii> q; q.push({i, j});
        while(q.size()){
            auto [x, y] = q.front(); q.pop();
            for(int dir = 0; dir < 4; dir++){
                int nx = x+dx[dir], ny = y+dy[dir];
                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if(board[nx][ny]){
                    board[nx][ny] = 0;
                    cnt++;
                    q.push({nx, ny});
                }
            }
        }
        ans.push_back(cnt);
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    if(ans.size()) for(int i = 0; i < ans.size(); i++) cout << ans[i] << '\n';
    return 0;
}