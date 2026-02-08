#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    if(n == 4 || n == 7) return !(cout << -1);
    int q = n / 5, r = n % 5;
    if(r == 0) cout << q;
    else if(r == 1 || r == 3) cout << q+1;
    else cout << q+2;
    return 0;
}