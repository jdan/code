#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool isSquare(long long int n) {
  return (sqrt(n) == (int)(sqrt(n)));
}

int d = 2;
long long int _max = 0LL;
int maxd = 0;

int main() {
    ofstream myfile;
    myfile.open("numbers.txt");
    while (d < 1001) {
      //cout << d << endl;
      if (isSquare(d)) {
        d += 1;
      } else {
        long long int y = 1LL;
        while(true) {
          long long int x2 = (d * (y * y) + 1);
          if (isSquare(x2)) {
            cout << (long long int)sqrt(x2) << "^2 - " << d << " * " << y << "^2 = 1" << endl;
            myfile << (long long int)sqrt(x2) << "^2 - " << d << " * " << y << "^2 = 1" << endl;
            if ((long long int)sqrt(x2) > _max) {
              cout << "**** NEW MAX ****" << endl;
              _max = (long long int)sqrt(x2);
              maxd = d;
            }
            break;
          } else {
            y += 1;
          }
        }
        d += 1;
      }
    }
    myfile.close();
    cout << maxd;
}
