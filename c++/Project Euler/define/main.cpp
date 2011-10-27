#include <iostream>

#define DUZ if (
#define KTHANX }
#define NAH } else {
#define EQUALZ ==
#define SAYZ cout <<
#define GETME cin >>
#define MAKEINT int
#define NULINE endl

using namespace std;

int main() {
  MAKEINT num, num2;
  SAYZ "NUMBA?: ";
  GETME num;
  SAYZ NULINE << "IZ 5?" << NULINE;
  DUZ num EQUALZ 5 ) {
    SAYZ "YUP";
  NAH
    SAYZ "NOPE";
  KTHANX
  SAYZ NULINE
  GETME num2;
}
