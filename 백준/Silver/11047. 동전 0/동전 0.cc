#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, k; cin >> n >> k;
    vector<int> a(n); int ans = 0;
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = n-1; i >= 0; i--){
        if(!k) break;
        ans += k/a[i];
        k %= a[i];
    }
    cout << ans;
    return 0;
}