#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    stack<int> st;
    while(n--){
        string cmd; cin >> cmd;
        if(cmd == "push"){
            int x; cin >> x;
            st.push(x);
        }
        else if(cmd == "pop"){
            if(st.size()){
                cout << st.top() << '\n'; st.pop();
            }
            else cout << -1 << '\n';
        }
        else if(cmd == "size") cout << st.size() << '\n';
        else if(cmd == "empty") cout << (st.size() ? 0 : 1) << '\n';
        else if(cmd == "top") cout << (st.size() ? st.top() : -1) << '\n';
    }
    return 0;
}