#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    string s; cin >> s;
    int cnt, ans, i; cnt = ans = 0; i = 1;
    while(i < m-1){
        if(s[i-1] == 'I' && s[i] == 'O' && s[i+1] == 'I'){
            cnt++;
            if(cnt >= n) ans++;
            i += 2;
        }
        else{
            cnt = 0;
            i++;
        }
    }
    cout << ans;
    return 0;
}