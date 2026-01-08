#include<bits/stdc++.h>
using namespace std;
using ll = long long;

vector<int> ret, rev;

void SA(string s){
	int n = s.size(); int m = max(n, 1024)+1;
	vector<int> sa(n), r(2*n), nr(2*n), cnt(m), idx(n);
	for(int i = 0; i < n; i++) sa[i] = i, r[i] = s[i]-'0'+1;
	for(int d = 1; d < n; d <<= 1){
		auto cmp = [&](int i, int j){
			return r[i] < r[j] || r[i] == r[j] && r[i+d] < r[j+d];
		};
		for(auto& i : cnt) i = 0;
		for(int i = 0; i < n; i++) cnt[r[i+d]]++;
		for(int i = 1; i < m; i++) cnt[i] += cnt[i-1];
		for(int i = n-1; i >= 0; i--) idx[--cnt[r[i+d]]] = i;
		for(auto& i : cnt) i = 0;
		for(int i = 0; i < n; i++) cnt[r[i]]++;
		for(int i = 1; i < m; i++) cnt[i] += cnt[i-1];
		for(int i = n-1; i >= 0; i--) sa[--cnt[r[idx[i]]]] = idx[i];
		nr[sa[0]] = 1;
		for(int i = 1; i < n; i++) nr[sa[i]] = nr[sa[i-1]] + cmp(sa[i-1], sa[i]);
		for(int i = 0; i < n; i++) r[i] = nr[i];
	}
	rev.resize(n/2); ret.resize(n/2); int ii = 0;
	for(int i : sa) if(i < n/2){
		rev[i] = ii;
		ret[ii++] = i;
	}
}
int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	int n, k; cin >> n >> k;
	string s; cin >> s; s = s+s;
	if(n == k){
		int ans = 0;
		for(int i = 0; i < n; i++) ans = max(ans, s[i]-'0');
		return !(cout << ans);
	}
	SA(s);
	int l = 0, r = n;
	while(l < r){
		int mid = l+r>>1;
		bool flag = 0;
		for(int x = 0; x < (n-1)/k+1; x++){
			int cnt = 0; int now = x;
			while(now < x+n){
				if(rev[now%n] <= rev[ret[mid]]) now++;
				now += (n-1)/k;
				cnt++;			
			}
			if(cnt <= k){
				flag = 1;
				break;
			}
		}
		if(flag) r = mid;
		else l = mid+1;
	}
	cout << s.substr(ret[l], (n-1)/k+1);
}