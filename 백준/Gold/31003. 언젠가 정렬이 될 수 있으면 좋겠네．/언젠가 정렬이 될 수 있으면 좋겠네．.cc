#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<vector<int>> e(n);
    vector<int> deg(n, 0), a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
        for(int j = 0; j < i; j++){
            if(gcd(a[j], a[i]) != 1){
                e[j].push_back(i);
                deg[i]++;
            }
        }
    }
    priority_queue<pii> pq;
    for(int i = 0; i < n; i++) if(!deg[i]) pq.push({-a[i], i});
    while(pq.size()){
        int cur = pq.top().second; pq.pop();
        cout << a[cur] << ' ';
        for(auto& nxt : e[cur]){
            if(!(--deg[nxt])) pq.push({-a[nxt], nxt});
        }
    }
    return 0;
}