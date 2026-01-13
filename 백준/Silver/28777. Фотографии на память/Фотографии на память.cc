#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int a[1010], dp[1010];

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    for(int i = 4; i <= n+3; i++) cin >> a[i];
    sort(a+4, a+n+4);
    for(int i = 4; i <= n+3; i++){
        dp[i] = dp[i-1]+1;
        if(a[i]-a[i-1] <= 20) dp[i] = min(dp[i], dp[i-2]+1);
        if(a[i]-a[i-2] <= 10) dp[i] = min(dp[i], dp[i-3]+1);
    }
    cout << dp[n+3];
    return 0;
}