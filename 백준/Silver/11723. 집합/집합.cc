#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int m, s; cin >> m; s = 0;
    while(m--){
        string cmd; cin >> cmd;
        if(cmd == "all") s = (1<<21)-1; 
        else if(cmd == "empty") s = 0;
        else{
            int x; cin >> x;
            if(cmd == "add") s |= (1<<x);
            else if(cmd == "remove") s &= ~(1<<x);
            else if(cmd == "check") cout << (s & (1<<x) ? 1 : 0) << '\n';
            else if(cmd == "toggle") s ^= (1<<x);
        }
    }
    return 0;
}