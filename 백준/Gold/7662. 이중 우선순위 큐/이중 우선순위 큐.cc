#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pli = pair<ll, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        int k; cin >> k;
        priority_queue<pli> max_pq;
        priority_queue<pli, vector<pli>, greater<pli>> min_pq;
        vector<int> visited(k, 0);
        for(int i = 0; i < k; i++){
            char c; ll v; cin >> c >> v;
            if(c == 'I'){
                max_pq.push({v, i});
                min_pq.push({v, i});
                visited[i] = 1;
            }
            else{
                if(v == 1){
                    while(max_pq.size() && !visited[max_pq.top().second]) max_pq.pop();
                    if(max_pq.size()){visited[max_pq.top().second] = 0; max_pq.pop();}
                }
                else{
                    while(min_pq.size() && !visited[min_pq.top().second]) min_pq.pop();
                    if(min_pq.size()){visited[min_pq.top().second] = 0; min_pq.pop();}
                }
            }
        }
        while(max_pq.size() && !visited[max_pq.top().second]) max_pq.pop();
        while(min_pq.size() && !visited[min_pq.top().second]) min_pq.pop();
        if(max_pq.empty() || min_pq.empty()) cout << "EMPTY\n";
        else cout << max_pq.top().first << ' ' << min_pq.top().first << '\n';
    }
    return 0;
}