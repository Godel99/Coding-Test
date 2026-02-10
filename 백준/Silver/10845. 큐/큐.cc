#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    queue<int> q;
    while(n--){
        string cmd; cin >> cmd;
        if(cmd == "push"){
            int x; cin >> x;
            q.push(x);
        }
        else if(cmd == "pop"){
            if(q.size()){
                cout << q.front() << '\n'; q.pop();
            }
            else cout << -1 << '\n';
        }
        else if(cmd == "size") cout << q.size() << '\n';
        else if(cmd == "empty") cout << (q.size() ? 0 : 1) << '\n';
        else if(cmd == "front") cout << (q.size() ? q.front() : -1) << '\n';
        else if(cmd == "back") cout << (q.size() ? q.back() : -1) << '\n';
    }
    return 0;
}