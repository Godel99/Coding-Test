#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n, m, k; cin >> n >> m >> k;
    if(n == m) return !(cout << -1);
    for(int i = 1; i < k; i++) cout << i << ' ';
    cout << n << ' ';
    for(int i = k; i < m; i++) cout << i << ' ';
    for(int i = n-1; i >= m; i--) cout << i << ' ';
	return 0;
}