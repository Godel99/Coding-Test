#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    vector<int> dp(n, 1);
    int ans = 1;
    for(int i = 0; i < n; i++) for(int j = 0; j < i; j++){
        if(a[j] < a[i]) dp[i] = max(dp[i], dp[j]+1);\
        if(ans < dp[i]) ans = dp[i];
    }
    cout << ans;
    return 0;
}