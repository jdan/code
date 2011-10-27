#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int primes = 4;
    for (int i = 1; i < 50000000; i++) {
        int a = 6 * i + 1;
        if (a % 5 != 0 && a % 7 != 0) {
            primes++;
        }
        int b = 6 * i -1;
        if (b % 5 != 0 && b % 7 != 0) {
            primes++;
        }
    }

    cout << primes;
}
