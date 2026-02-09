#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> cards(n);
    for(int i = 0; i < n; i++) cin >> cards[i];
    sort(cards.begin(), cards.end());
    int m; cin >> m;
    for(int i = 0; i < m; i++){
        int x; cin >> x;
        cout << upper_bound(cards.begin(), cards.end(), x) - lower_bound(cards.begin(), cards.end(), x) << ' ';
    }
    return 0;
}