#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, k; cin >> n >> k;
    priority_queue<tuple<int, ll, int>> pq;
    vector<int> cnt(k+1, 0);
    vector<tuple<int, int, ll, int>> g;
    g.reserve(n);
    for(int i = 0; i < n; i++){
        int x, y, c; ll p; cin >> x >> y >> p >> c;
        g.push_back({x, y, p, c});
    }
    sort(g.begin(), g.end());
    ll ans, cur; ans = cur = 0;
    int maxh = 123456789;
    for(int i = 0; i < n; i++){
        auto [x, y, p, c] = g[i];
        pq.push({y, p, c});
        cur += p;
        if(!cnt[c]) cnt[0]++;
        cnt[c]++;
        if(i == n-1 || get<0>(g[i+1]) != x){
            while(pq.size()){
                auto [yy, pp, cc] = pq.top();
                if(cnt[0] != k && yy <= maxh) break;
                pq.pop();
                cur -= pp;
                cnt[cc]--;
                if(!cnt[cc]) cnt[0]--;
                maxh = min(maxh, yy-1);
            }
            ans = max(ans, cur);
        }
    }
    cout << ans;
    return 0;
}