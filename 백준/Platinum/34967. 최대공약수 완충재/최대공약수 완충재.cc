#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    int i = 1, j = 19999;
    for(int k = 0; k < n-1; k++){
        cout << i*j << ' ';
        if(k&1) i++;
        else j--;
    }
    if(n < 20000) cout << i*j;
    else cout << 10000000;
    return 0;
}