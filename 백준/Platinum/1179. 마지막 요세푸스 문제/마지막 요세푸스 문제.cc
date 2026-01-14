#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll josephus(ll n, ll k){
    if(n == 1) return 0;
    if(n < k) return (josephus(n-1, k)+k)%n;
    ll l = josephus(n-n/k, k) - n%k;
    if(l < 0) return l+n;
    return l+l/(k-1);
}

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    ll n, k; cin >> n >> k; if(k == 1) cout << n; else cout << josephus(n, k)+1;
}