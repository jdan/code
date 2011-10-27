#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool isprime(int n) {
  if (n == 2) {
    return true;
  } else if (n % 2 == 0) {
    return false;
  } else {
    for (int i = 3; i <= sqrt(n); i += 2) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}

int main() {
  ofstream file;
  file.open("primes.txt");
  int n = 2;
  while (true) {
    if (isprime(n)) {
      cout << n << endl;
      file << n << endl;
    }
    n++;
  }
  file.close();
}