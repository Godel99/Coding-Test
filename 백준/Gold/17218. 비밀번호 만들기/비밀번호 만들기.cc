#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    string a, b; cin >> a >> b;
    int n = a.size(), m = b.size();
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(a[i-1] == b[j-1]) dp[i][j] = dp[i-1][j-1]+1;
            else dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
    stack<char> ans;
    while(n && m){
        if(a[n-1] == b[m-1]){
            ans.push(a[n-1]);
            n--;
            m--;
        }
        else if(dp[n-1][m] > dp[n][m-1]) n--;
        else m--;
    }
    while(ans.size()){
        cout << ans.top();
        ans.pop();
    }
    return 0;
}