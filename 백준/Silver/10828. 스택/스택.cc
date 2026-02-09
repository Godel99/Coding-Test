#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    stack<int> st;
    while(n--){
        string com; cin >> com;
        if(com == "push"){
            int x; cin >> x;
            st.push(x);
        }
        else if(com == "pop"){
            if(st.size()){
                cout << st.top() << '\n'; st.pop();
            }
            else cout << -1 << '\n';
        }
        else if(com == "size") cout << st.size() << '\n';
        else if(com == "empty") cout << (st.size() ? 0 : 1) << '\n';
        else if(com == "top") cout << (st.size() ? st.top() : -1) << '\n';
    }
    return 0;
}