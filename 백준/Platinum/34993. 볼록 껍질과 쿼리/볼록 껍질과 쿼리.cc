#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using ai6 = array<int, 6>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n;
    vector<pii> pt(n+1);
    vector<ai6> qry(n+1);
    auto chk = [&](int i, int j, int idx){
        return qry[i][j] == pt[idx].first && qry[i][j+1] == pt[idx].second;
    };
    for(int i = 3; i <= n; i += 2){
        cout << "? 3 " << i-2 << ' ' << i-1 << ' ' << i << endl;
        cin >> m; for(int j = 0; j < 6; j++) cin >> qry[i][j];
    }
    for(int i = 5; i <= n; i += 2){
        for(int j = 0; j < 6; j += 2){
            for(int k = 0; k < 6; k += 2){
                if(qry[i-2][j] == qry[i][k] && qry[i-2][j+1] == qry[i][k+1]){
                    pt[i-2]= {qry[i][k], qry[i][k+1]};
                }
            }
            if(i != 5){
                for(int j = 0; j < 6; j += 2){
                    for(int k = 0; k < 6; k += 2){
                        if(!chk(i-2, j, i-4) && !chk(i-2, j, i-2)){
                            pt[i-3] = {qry[i-2][j], qry[i-2][j+1]};
                        }
                    }
                }
            }
        }
    }
    if(n&1){
        cout << "? 3 1 5 " << n << endl;
        cin >> m; for(int j = 0; j < 6; j++) cin >> qry[1][j];
        for(int j = 0; j < 6; j += 2){
            for(int k = 0; k < 6; k += 2){
                if(qry[1][j] == qry[3][k] && qry[1][j+1] == qry[3][k+1]){
                    pt[1] = {qry[1][j], qry[1][j+1]};
                }
            }
        }
        for(int j = 0; j < 6; j += 2){
            if(!chk(3, j, 1) && !chk(3, j, 3)){
                pt[2] = {qry[3][j], qry[3][j+1]};
            }
        }
        for(int j = 0; j < 6; j += 2){
            for(int k = 0; k < 6; k += 2){
                if(qry[1][j] == qry[n][k] && qry[1][j+1] == qry[n][k+1]){
                    pt[n] = {qry[1][j], qry[1][j+1]};
                }
            }
        }
        for(int j = 0; j < 6; j += 2){
            if(!chk(n, j, n) && !chk(n, j, n-2)){
                pt[n-1] = {qry[n][j], qry[n][j+1]};
            }
        }
    }
    else{
        cout << "? 3 1 " << n-1 << ' ' << n << endl;
        cin >> m; for(int j = 0; j < 6; j++) cin >> qry[1][j];
        for(int j = 0; j < 6; j += 2){
            for(int k = 0; k < 6; k += 2){
                if(qry[1][j] == qry[3][k] && qry[1][j+1] == qry[3][k+1]){
                    pt[1] = {qry[1][j], qry[1][j+1]};
                }
            }
        }
        for(int j = 0; j < 6; j += 2){
            if(!chk(3, j, 1) && !chk(3, j, 3)){
                pt[2] = {qry[3][j], qry[3][j+1]};
            }
        }
        for(int j = 0; j < 6; j += 2){
            for(int k = 0; k < 6; k += 2){
                if(qry[1][j] == qry[n-1][k] && qry[1][j+1] == qry[n-1][k+1]){
                    pt[n-1] = {qry[1][j],  qry[1][j+1]};
                }
            }
        }
        for(int j = 0; j < 6; j += 2){
            if(!chk(n-1, j, n-1) && !chk(n-1, j, n-3)){
                pt[n-2] = {qry[n-1][j], qry[n-1][j+1]};
            }
        }
        for(int j = 0; j < 6; j += 2){
            if(!chk(1, j, 1) && !chk(1, j, n-1)){
                pt[n] = {qry[1][j], qry[1][j+1]};
            }
        }
    }
    cout << "! "; for(int i = 1; i <= n; i++) cout << pt[i].first << ' ' << pt[i].second << ' '; cout << endl;
    return 0;
}