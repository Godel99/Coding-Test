#include<bits/stdc++.h>
using namespace std;
using ll=long long;

int solution(vector<int> a) {
    int n = a.size();
    if (n <= 2) return n;

    unordered_set<int> survive;

    int cur_min = INT_MAX;
    for (int i = 0; i < n; i++){
        if (a[i] < cur_min){
            cur_min = a[i];
            survive.insert(i);
        }
    }

    cur_min = INT_MAX;
    for (int i = n-1; i > -1; i--){
        if (a[i] < cur_min){
            cur_min = a[i];
            survive.insert(i);
        }
    }

    return survive.size();
}