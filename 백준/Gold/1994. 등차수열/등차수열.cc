#include<bits/stdc++.h>
using namespace std;
map<int, int> cnt;
vector<int> v;
int d[2020][2020];

int dp(int i, int j){
	int& ret = d[i][j];
	if(ret) return ret;
	ret = 2;
	int nxt = lower_bound(v.begin()+j, v.end(), 2*v[j]-v[i]) - v.begin();
	if(v[nxt] != 2*v[j]-v[i]) return ret;
	return ret = 1 + dp(j, nxt);
}

int main(){
	cin.tie(0);cout.tie(0);ios::sync_with_stdio(0);
	int n, ans = 2; cin >> n;
	if(n == 1) return !(cout << 1);
	for(int i = 0; i < n; i++){
		int k; cin >> k;
		if(cnt.find(k) != cnt.end()){
			cnt[k]++;
			ans = max(ans, cnt[k]);
		}
		else{
			cnt.insert({k,1});
			v.push_back(k);
		}
	}
	sort(v.begin(), v.end());
	for(int i = 0; i < v.size(); i++){
		for(int j = i+1; j < v.size(); j++){
			ans = max(ans, dp(i, j));
		}
	}
	cout << ans;
}