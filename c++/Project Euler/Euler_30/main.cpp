#include <iostream>
#include <cmath>
#include <sstream>

using namespace std;

int main()
{
    stringstream ss;
    string num;
    long long int sum = 0.0;
    long total = 0.0;
    for (int i = 0; i < 10000; i++) {
        ss << i;
        num = ss.str();
        for (int c = 0; c < num.length(); c++) {
            sum += (long long int) pow((long) num[c], 5.0);
        }
        cout << sum << "\n";
        if (sum == i) {
            total += sum;
        }
    }
    cout << "Total: " << total;
}
