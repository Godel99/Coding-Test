#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<vector<int>> g(n, vector<int>(n));
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) cin >> g[i][j];
    for(int k = 0; k < n; k++) for(int i = 0; i < n; i++){
        if(g[i][k]){
            for(int j = 0; j < n; j++){
                if(g[k][j]) g[i][j] = 1;
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++) cout << g[i][j] << ' ';
        cout << '\n';
    } 
    return 0;
}