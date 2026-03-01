#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, k; cin >> n >> k;
    if(n == k){cout << 0; return 0;}
    int maxl = (n > k ? n : k)+2;
    vector<int> dp(maxl, 0);
    queue<int> q; q.push(n);
    while(q.size()){
        int cur = q.front(); q.pop();
        for(int nxt : {cur-1, cur+1, cur*2}){
            if(0 <= nxt && nxt < maxl && !dp[nxt]){
                dp[nxt] = dp[cur]+1;
                q.push(nxt);
            }
        }
    }
    cout << dp[k];
    return 0;
}