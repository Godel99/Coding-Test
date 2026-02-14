#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> p(n);
    for(int i = 0; i < n; i++) cin >> p[i];
    sort(p.begin(), p.end());
    int ans = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j <= i; j++) ans += p[j];
    }
    cout << ans;
    return 0;
}