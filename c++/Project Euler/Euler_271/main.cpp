#include <iostream>
#include <cmath>

using namespace std;

int main() {
  long long int s = 13082761331670030LL;
  int start = 235631;
  long long int total = 0LL;
  int i = start;

  while(true) {
    total += (int)((int)pow(i,3.0) % (int)s == 1);
    i++;
    if (i > s) { break; }
    if (i % 1000000 == 0) { cout << ((double)i / s) << endl; }
  }

  cout << total;
}
