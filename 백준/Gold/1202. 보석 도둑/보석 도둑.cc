#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, k; cin >> n >> k;
    vector<pii> gems(n);
    for(int i = 0; i < n; i++) cin >> gems[i].first >> gems[i].second;
    vector<ll> bags(k);
    for(int i = 0; i < k; i++) cin >> bags[i];
    sort(gems.begin(), gems.end());
    sort(bags.begin(), bags.end());
    priority_queue<int, vector<int>> pq;
    int idx = 0; ll ans =0;
    for(auto& bag: bags){
        while(idx < n && gems[idx].first <= bag){
            pq.push(gems[idx].second);
            idx++;
        }  
        if(!pq.empty()){
            ans += pq.top(); pq.pop();
        }
    }
    cout << ans;
    return 0;
}