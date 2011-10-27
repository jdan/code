#include <iostream>
#include <cmath>

using namespace std;

int factors(int n) {
    int total = 0;
    for (int i = 1; i < (int)sqrt(n) + 1; i++) {
        if (n % i == 0) {
            total++;
            if (i * i != n) {
                total++;
            }
        }
    }
    return total;
}

int main()
{
    int total = 1;
    int now = 2;
    int nxt = 2;

    for (int i = 3; i < 10000000; i++) {
        now = nxt;
        nxt = factors(i+1);
        if (now == nxt) {
            total++;
        }
    }

    cout << "Total: " << total;
}
