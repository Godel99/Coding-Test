#include<bits/stdc++.h>
using namespace std;
using ll = long long;

bool is_squ(int n){
        int t = (int)sqrt(n);
        return n == t*t;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    if(is_squ(n)) return !(cout << 1);
    for(int i = 1; i*i <= n; i++){
        if(is_squ(n-i*i)) return !(cout << 2);
    }
    for(int i = 1; i*i <= n; i++){
        for(int j = 1; i*i+j*j <= n; j++){
            if(is_squ(n-i*i-j*j)) return !(cout << 3);
        }
    }
    cout << 4;
    return 0;
}