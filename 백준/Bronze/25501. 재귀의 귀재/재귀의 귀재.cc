#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

pii recursion(string& s, int l, int r){
    if(l >= r) return {1, l+1};
    else if(s[l] != s[r]) return {0, l+1};
    else return recursion(s, l+1, r-1);
}

pii isPalindrome(string& s){
    return recursion(s, 0, s.length()-1);
}

int main(){
	cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
	int n; cin >> n;
	for(int i = 0; i < n; i++) {
		string s; cin >> s;
		auto [r, c] = isPalindrome(s);
		cout << r << ' ' << c << '\n';
	}
    return 0;
}