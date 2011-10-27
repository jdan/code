#include <iostream>

using namespace std;

int relprime(int n) {
    int num = 0;
    for (int i = 2; i <= n; i++) {
        if (n % i != 0) {
            num++;
        }
    }
    return num + 1;
}

int main()
{
    float max = 0.0;
    int max_n = 0;
    for (int i = 8; i <= 1000000; i++) {
        if ((float)i / relprime(i) > max) {
            max = (float)i / relprime(i);
            max_n = i;
        }
        if (i % 5000 == 0) {
            cout << i << "-> Max: " << max_n << ": " << max << endl;
        }
    }
    cout << "Max: " << max_n << ": " << max;
}
