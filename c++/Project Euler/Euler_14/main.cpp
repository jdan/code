#include <iostream>
#include <math.h>

using namespace std;

/**
++ Author: Jordan Scales
++ Date:   10/3/09

What is the value of the first triangle number to have over five hundred divisors?

*/

int main()
{
    int divisors = 0;
    int step = 1;
    int number = 1;
    while (divisors < 500) {
        step++;
        number += step;
        divisors = 0;
        if (number % 2 == 0) {
            for (int i = 1; i <= sqrt(number); i++) {
                if (number % i == 0) {
                    divisors++;
                }
            }
            divisors *= 2;
            cout << number << ": " << divisors << "\n";
        }
    }
}
