#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 1234567891;

ll pw(ll n, ll r){
	ll ret = 1;
	while(r){
		if(r&1) ret = ret*n%MOD;
		n = n*n%MOD;
		r>>=1;
	}
	return ret;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    string s; cin >> s;
    int h = 0;
    for(int i = 0; i < n; i++){
        h = (h+(s[i]-'a'+1)*pw(31, i)) % MOD;
    }
    cout << h;
    return 0;
}