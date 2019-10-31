#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;
int maxProfit(vector<int>& prices, int fee){
    int n = prices.size(), empty = 0, hold = -prices[0]-fee;
    for(int i = 1; i < n; i++) {
        // Order doesn't matter: empty then hold, or hold then empty, works.
        // For empty then hold:
        // "empty" will only change when selling, but we will not buy the stock again 
        // on that day after selling due to transaction fee, so it is safe to
        // use updated (in fact, intact) "empty" value for "empty - prices[i] - fee".
        // i.e., when empty = hold + prices[i],
        //       empty - prices[i] - fee = hold - fee < hold
        // Vice versa for hold then empty.
        empty = max(empty, hold + prices[i]); // sell
        hold = max(hold, empty - prices[i] - fee); // buy  
        printf("empty = %d, hold = %d,",empty, hold);
    }
    // Return "empty" because the profit will always be higher
    // compared to holding one unsold stock.
    return empty;
}

int main(){
    vector<int> p {1, 3, 2, 8, 4, 9};
    int fee;
    fee = 2;
    maxProfit(p, fee);

    return 0;
}
