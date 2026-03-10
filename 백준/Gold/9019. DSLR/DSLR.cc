#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pic = pair<int, char>;
int mod = 10000;
pic par[10000];

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int a, b; cin >> a >> b;
        queue<int> q; q.push(a);
        memset(par, -1, sizeof(par));
        par[a] = {a, '\0'};
        while(q.size()){
            int cur = q.front(); q.pop();
            if(cur == b) break;
            int nxt = (cur*2)%mod;
            if(par[nxt].first == -1){
                par[nxt] = {cur, 'D'};
                q.push(nxt);
            }
            nxt = cur ? cur-1 : 9999;
            if(par[nxt].first == -1){
                par[nxt] = {cur, 'S'};
                q.push(nxt);
            }
            nxt = (cur%1000)*10+(cur/1000);
            if(par[nxt].first == -1){
                par[nxt] = {cur, 'L'};
                q.push(nxt);
            }
            nxt = (cur%10)*1000+(cur/10);
            if(par[nxt].first == -1){
                par[nxt] = {cur, 'R'};
                q.push(nxt);
            }
        }
        string ans = "";
        while(b != a){
            ans += par[b].second;
            b = par[b].first;
        }
        reverse(ans.begin(), ans.end());
        cout << ans << '\n';
    }
    return 0;
}