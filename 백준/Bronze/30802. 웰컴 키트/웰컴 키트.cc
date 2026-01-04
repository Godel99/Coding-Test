#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, c, t, p; cin >> n;
    vector<int> candidate(6);

    for (int i = 0; i < 6; i++){
        cin >> c;
        candidate.push_back(c);
    }
    cin >> t >> p;
    int total = 0;
    for (auto c : candidate){
        if (c == 0) continue;
        total += (c + t - 1) / t;
    }

    cout << total << endl;
    cout << n / p << ' ' << n % p;
}