#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        string s; cin >> s;
        stack<char> st;
        bool flag = 1;
        for(auto c : s){
            if(c == '(') st.push(c);
            else if(st.size()) st.pop();
            else flag = 0;
        }
        if(flag && st.empty()) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}