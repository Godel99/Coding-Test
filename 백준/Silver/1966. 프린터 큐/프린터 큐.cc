#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        queue<pii> q;
        priority_queue<int> pq;
        for(int i = 0; i < n; i++){ 
            int x; cin >> x;
            q.push({x, i});
            pq.push(x);
        }
        int cnt = 0;
        while(q.size()){
            auto [v, i] = q.front(); q.pop();
            if(v == pq.top()){
                cnt++;
                pq.pop();
                if(i == m) {
                    cout << cnt << '\n';
                    break;
                }
            }
            else q.push({v, i});
        }
    }
    return 0;
}