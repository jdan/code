#include <iostream>

using namespace std;

long long int fact(int n) {
    if (n <= 1) {
        return n;
    } else {
        return (long long int)n * fact(n-1);
    }
}

int main() {
    int trials, n;
    cin >> trials;
    for (int i = 0; i < trials; i++) {
        cin >> n;
        cout << fact(n) << endl;
    }
}
