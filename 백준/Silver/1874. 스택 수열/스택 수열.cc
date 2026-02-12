#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, nx; cin >> n; nx = 1;
    stack<int> st;
    string ans = "";
    ans.reserve(n*4);
    while(n--){
        int x; cin >> x;
        while(nx <= x){
            ans += "+\n";
            st.push(nx++);
        }
        if(st.size() && st.top() == x){
            ans += "-\n";
            st.pop();
        }
        else return !(cout << "NO");
    }
    cout << ans;
    return 0;
}