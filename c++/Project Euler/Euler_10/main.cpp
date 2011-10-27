#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(int n) {
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= sqrt(n); i+=2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    long long int total = 0.0;
    for (int i = 2; i < 2000000; i++) {
        if (isPrime(i)) {
            total += i;
        }
    }
    cout << total;
}
