#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    int l = 1, r = 1;
    
    if(n==1){
        cout << 1;
        return 0;
    }
    
    while(r < n){
        r += l*6;
        l++;
    }
    cout << l;
    return 0;
}