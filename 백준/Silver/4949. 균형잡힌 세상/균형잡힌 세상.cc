#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    while(true){
        string s; getline(cin, s);
        if(s == ".") break;
        stack<char> st;
        bool flag = true;
        for(char c : s){
            if(c == '('  || c == '[') st.push(c);
            else if(c == ')'){ 
                if(st.empty() || st.top() != '(') {
                    flag = false;  break;
                }
                st.pop();
            }
            else if(c == ']'){
                if(st.empty() || st.top() != '[') {
                    flag = false; break;
                }  
                st.pop(); 
            }     
        }
        if(flag && st.empty()) cout << "yes\n";
        else cout << "no\n";
    }
    return 0;
}