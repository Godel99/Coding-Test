#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, f = 5, cnt = 0; cin >> n;
    while(f <= n){
        cnt += n / f;
        f *= 5;
    }
    cout << cnt;
    return 0;
}