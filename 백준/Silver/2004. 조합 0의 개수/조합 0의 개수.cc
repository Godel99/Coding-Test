#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int cp(ll n, ll m){
    int cnt = 0;
    while(n >= m){
        n /= m;
        cnt += n;
    }
    return cnt;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    ll n, m; cin >> n >> m;
    int cnt2 = cp(n, 2)-cp(m, 2)-cp(n-m, 2);
    int cnt5 = cp(n, 5)-cp(m, 5)-cp(n-m, 5);
    cout << min(cnt2, cnt5);
    return 0;
}