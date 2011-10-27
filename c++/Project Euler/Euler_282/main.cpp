#include <iostream>
#include <cmath>

using namespace std;

int a (int m, int n) {
   if (m == 0) {
      return n+1;
   } else {
      if (n == 0) {
         return a(m-1, 1);
      } else {
         return a(m-1, a(m, n-1));
      }
   }
}

int main() {
   long long int total = 0LL;
   for (int n = 0; n <= 6; n++) {
      total += (long long int)a(n, n);
   }
   cout << total % (long long int)pow(14.0, 8.0);
   return 0;
}
