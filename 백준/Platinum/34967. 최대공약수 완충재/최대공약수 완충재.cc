#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int i, j; i = 3, j = 14001;
    vector<int> res;
    while(i != j){
        res.push_back(i*j);
        res.push_back(i*j);
        if(i+j == 14004) j -= 2;
        else i += 2;
    }
    res.pop_back();
    int n, m = res.size(); cin >> n;
    for(int k = 0; k < n; k++){
        if(k < m) cout << res[k]*2 << ' ';
        else cout << res[m*2-1-k] << ' ';
    }
    return 0;
}