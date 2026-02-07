#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    while(n--){
        int x, y; cin >> x >> y;
        int k; cin >> k;
        int g = 0;
        for(int i = 0; i < k; i++){
            int t; cin >> t;
            g = gcd(t, g);
        }
        if(x%g || y%g) cout << "Gave up\n";
        else cout << "Ta-da\n";
    }
    return 0;
}