#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int k; cin >> k;
    stack<int> st;
    while(k--){
        int x; cin >> x;
        if(x) st.push(x);
        else st.pop();
    }
    ll ans = 0;
    while(st.size()){
        ans += st.top();
        st.pop();
    }
    cout << ans;
    return 0;
}