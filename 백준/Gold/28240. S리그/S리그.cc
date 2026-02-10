#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, a, b, c, d; cin >> n >> a >> b >> c >> d;
    for(int i = 1; i < n; i++){
        cout << i << ' ';
        if(i == a || i == b) cout << 1 << '\n';
        else if(i == c || i == d) cout << -1 << '\n';
        else cout << 0 << '\n';
    }
    cout << n << ' ';
    if(n == a || n == b) cout << 2*n << '\n';
    else cout << -2*n << '\n';
    return 0;
}