#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    ll low, high, cur; cin >> low >> high; cur = high;
    for(int i = 2; i < n; i++){
        ll nxt, tmp = low; cin >> nxt;
        low = 2*cur-high;
        high = min(2*cur-tmp, nxt);
        cur = nxt;
    }
    cout << max(0ll, high-low+1);
    return 0;
}