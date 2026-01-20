#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    ll n, k; cin >> n >> k;
	ll ans = 0;
    for(int i = 1; i <= n; i++) ans = (ans+k)%i;
    cout << ans+1;
	return 0;
}