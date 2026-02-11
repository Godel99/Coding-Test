#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    char board[n][m];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++) cin >> board[i][j];
    }
    int min_d = 64;
    for(int i = 0; i < n-7; i++){
        for(int j = 0; j < m-7; j++){
            int d = 0;
            for(int r = i; r < i+8; r++){
                for(int c = j; c < j+8; c++){
                    if((r+c)%2){
                        if(board[r][c] != 'W') d++;
                    }
                    else{
                        if(board[r][c] != 'B') d++;
                    }
                }
            }
            min_d = min({min_d, d, 64-d}); 
        }
    }
    cout << min_d;
    return 0;
}