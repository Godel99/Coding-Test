#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
const int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};

char board[25][25];
ld d[25][25];

ld solved(){
    int r, c, sy, sx, s; cin >> r >> c >> sy >> sx >> s; sy++, sx++;
    ld p, q; cin >> p >> q;
    for(int i = 1; i <= r; i++) for(int j = 1; j <= c; j++){
        cin >> board[i][j];
        if(board[i][j] == 'A') d[i][j] = p;
        else d[i][j] = q; 
    }
    ld ans = 0;
    for(int l = 0; l < (1<<(2*s)); l++){
        int y = sy, x = sx; ld sump = 0; bool flag = 1;
        for(int i = 0; i < s; i++){
            int k = (l>>(i*2))&3;
            y += dy[k]; x += dx[k];
            if(y < 1 || y > r || x < 1 || x > c){
                flag = 0; continue;
            }
            sump += d[y][x];
            if(board[y][x] == 'A') d[y][x] *= 1-p;
            else d[y][x] *= 1-q;
        }
        if(flag) ans = max(ans, sump);
        y = sy, x = sx;
        for(int i = 0; i < s; i++){
            int k = (l>>(i*2))&3;
            y += dy[k]; x += dx[k];
            if(y < 1 || y > r || x < 1 || x > c) continue;
            sump += d[y][x];
            if(board[y][x] == 'A') d[y][x] = p;
            else d[y][x] = q;
        }
    }
    return ans;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int T; cin >> T; cout << fixed << setprecision(12);
    for(int i = 1; i <= T; i++) cout << "Case #" << i << ": " << solved() << '\n';
    return 0;
}