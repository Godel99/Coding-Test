#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    if(n == 1) return !(cout << n);
    int t = 2;
    while(t<<1 <= n) t <<= 1;
    if(t == n) cout << n;
    else cout << 2*(n-t);
    return 0;
}