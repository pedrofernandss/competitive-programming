#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;

    for(int i = 0; i < test_cases; i++){
    	int str_size, l = 0, r;
    	string str;

    	cin >> str_size;   	
    	cin >> str;

    	r = str_size - 1;

    	while(str[l] != str[r]){
    		l++;
    		r--;
    	}
    	int final_size = (r-l)+1;
    	if (final_size < 0) {
    	   final_size = 0;
    	}
    	cout << final_size << endl;

    }

    return 0;
}
