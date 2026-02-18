#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, a, l; cin >> n >> a >> l;
    vector<vector<int>> dp(n+1, vector<int>(l+1, -1));
    vector<vector<bool>> way(n+1, vector<bool>(l+1, false));
    vector<int> dam(n+1, 0);
    for(int i = 1; i <= l; i++) dp[0][i] = a;
    for(int i = 1; i <= n; i++){
        int x, y; cin >> x >> y;
        dam[i] = y;
        if(x == -1){
            for(int j = l; j > y; j--){
                if(dp[i-1][j] != -1){
                    dp[i][j-y] = dp[i-1][j];
                    way[i][j-y] = true;
                }
            }
        }
        else if(y == -1){
            for(int j = l; j > 0; j--){
                if(dp[i-1][j] != -1){
                    dp[i][j] = max(0, dp[i-1][j]-x);
                    way[i][j] = false;
                }
            }
        }
        else{
            for(int j = 1; j <= l; j++){
                if(dp[i-1][j] >= x){
                    dp[i][j] = dp[i-1][j]-x;
                    way[i][j] = false;
                }
                if(j > y && dp[i][j-y] < dp[i-1][j]){
                    dp[i][j-y] = dp[i-1][j];
                    way[i][j-y] = true;
                }
            }
        }
    }
    if(dp[n][1] != -1){
        cout << "YES\n";
        int life = 1;
        stack<char> st;
        for(int i = n; i > 0; i--){
            if(way[i][life]){
                st.push('L');
                life += dam[i];
            }
            else st.push('A');
        }
        while(st.size()){
            cout << st.top();
            st.pop();
        }
    }
    else cout << "NO\n";
    return 0;
}