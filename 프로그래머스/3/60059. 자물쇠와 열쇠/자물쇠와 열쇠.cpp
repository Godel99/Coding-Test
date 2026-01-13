#include<bits/stdc++.h>
using namespace std;
using ll = long long;

vector<vector<int>> rotate(vector<vector<int>> key){
    int n = key.size();
    vector<vector<int>> nk(n, vector<int>(n, 0));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++) nk[j][n-1-i] = key[i][j];
    }
    return nk;
}

bool isopen(int n, vector<vector<int>> board){
    for(int i = n; i < 2*n; i++){
        for(int j = n; j < 2*n; j++){
            if(board[i][j] != 1) return false;
        }
    }
    return true;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    int n, m; n = lock.size(); m = key.size();
    vector<vector<int>> board(n*3, vector<int>(n*3, 0));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++) board[i+n][j+n] = lock[i][j];
    }
    vector<vector<int>> cur = key;
    for(int r = 0; r < 4; r++){
        for(int x = 0; x < 2*n+1; x++){
            for(int y = 0; y < 2*n+1; y++){
                for(int i = 0; i < m; i++){
                    for(int j = 0; j < m; j++) board[x+i][y+j] += cur[i][j];
                }
                if(isopen(n, board)) return true;
                for(int i = 0; i < m; i++){
                    for(int j = 0; j < m; j++) board[x+i][y+j] -= cur[i][j];
                }
            }
        }
        cur = rotate(cur);
    }
    return false;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    return 0;
}