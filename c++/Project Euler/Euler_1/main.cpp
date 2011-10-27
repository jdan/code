#include <iostream>

using namespace std;

int main()
{
    int total = 0;
    for (int i = 0; i < 1000; i++) {
        total += i * (!(i%3) || !(i%5));
    }
    cout<<total<<endl;
}
