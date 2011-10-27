#include <iostream>
#include "LOL.h"

using namespace std;

int main() {
  MAKEINT num;
  SAYZ "NUMBA?: ";
  GETME num;
  DNTSTOPTIL num ISBIGRDEN 0 K
    SAYZ "IZ 5?" nd NULINE;
    DUZ num EQUALZ 5 K
      SAYZ "YUP";
    NAH
      SAYZ "NOPE";
    KTHANX
    SAYZ NULINE nd NULINE nd "NUMBA?: ";
    GETME num;
  KTHANX
}