#include<bits/stdc++.h>
using namespace std;
int ans[123];

int main(){
	int k, newk; cin >> k;
	for(int i = 1; i <= 100; i++){
		cout << "? ";
		for(int j = 1; j < i; j++) cout << 2;
		cout << 0;
		for(int j = i+1; j <= 100; j++) cout << 2;
		cout << endl;
		cin >> newk;
		if(k < newk) ans[i] = 2;
		else if(k == newk) ans[i] = 0;
		else ans[i] = 5;
	}
	cout << "! ";
	for(int i = 1; i <= 100; i++) cout << ans[i];
	cout << endl;
	return 0;
}