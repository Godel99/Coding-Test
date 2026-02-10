#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<int> cards(n);
    for(int i = 0; i < n; i++) cin >> cards[i];
    int msc = 0;
    
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            for(int k = j+1; k < n; k++){
                int sc = cards[i]+cards[j]+cards[k];
                if(sc <= m) msc = max(msc, sc);
            }
        }
    }
    cout << msc;
    return 0;
}