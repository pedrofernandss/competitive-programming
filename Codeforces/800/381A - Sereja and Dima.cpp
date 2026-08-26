#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int number_cards;
    vector<int> deck_cards;

    cin >> number_cards;

    for(int i = 0; i < number_cards; i++) {
        int aux;
        cin >> aux;
        deck_cards.push_back(aux);    
    }

    bool is_even;
    int left = 0, sp = 0, dp = 0;
    int right = deck_cards.size()-1;

    for(int i = 1; i <= number_cards; i++){
        
        if (i%2 == 0) {
            is_even = true;
        } else {
            is_even = false;
        }

        if (deck_cards[right] >= deck_cards[left]){
            if (is_even) {
                dp = dp + deck_cards[right];
            } else {
                sp = sp + deck_cards[right];
            }
            right--;
        } else {
            if (is_even) {
                dp = dp + deck_cards[left];
            } else {
                sp = sp + deck_cards[left];
            }
            left++;
        }    
    }

    cout << sp << " " << dp << endl;


    return 0;
}