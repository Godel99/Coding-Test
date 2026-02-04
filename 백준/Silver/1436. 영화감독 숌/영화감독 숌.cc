#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    int cnt = 0, i = 0, s;
    while(cnt < n){
        s = 666+i++;
        if (to_string(s).find("666") != string::npos) cnt++;
    }
    cout << s;
    return 0;
}