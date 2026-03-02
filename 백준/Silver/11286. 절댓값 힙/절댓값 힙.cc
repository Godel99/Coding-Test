#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    while(n--){
        int x; cin >> x;
        if(x) pq.push({abs(x), x});
        else{
            if(pq.empty()) cout << 0 << '\n';
            else {cout << pq.top().second << '\n'; pq.pop();}
        }
    }
    return 0;
}