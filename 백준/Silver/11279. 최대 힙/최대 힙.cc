#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    priority_queue<int> pq;
    while(n--){
        int x; cin >> x;
        if(x) pq.push(x);
        else{
            if(pq.size()){
                cout << pq.top() << '\n';
                pq.pop();
            }
            else cout << 0 << '\n';
        }
    }
    return 0;
}