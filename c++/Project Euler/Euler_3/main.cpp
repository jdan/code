// Project Euler 3 Solution by Jordan Scales [C++]
// 10/08/09
// What is the largest prime factor of the number 600851475143?

#include <iostream>

using namespace std;

int main()
{
  int div = 2;
  unsigned long long comp = 600851475143LLU;

  while (comp != div) {
    if (comp % div == 0) {
      comp = comp / div;
      div = 2;
    } else {
      div++;
    }
  }
  cout << "Largest Prime Factor: " << comp;
}

// OUTPUT== Largest Prime Factor: 6857
// TIME==   0.016s
