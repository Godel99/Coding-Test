#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<int> board(101, -1);
    vector<int> e(101);
    for(int i = 0; i <= 100; i++) e[i] = i;
    for(int i = 0; i < n+m; i++){
        int x, y; cin >> x >> y;
        e[x] = y;
    }
    board[1] = 0;
    queue<int> q; q.push(1);
    while(q.size()){
        int cur = q.front(); q.pop();
        for(int i = 1; i <= 6; i++){
            int nxt = cur+i;
            if(nxt <= 100){
                nxt = e[nxt];
                if(board[nxt] == -1){
                    board[nxt] = board[cur]+1;
                    q.push(nxt);
                }
            }
        }
    }
    cout << board[100];
    return 0;
}