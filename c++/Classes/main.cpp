#include <iostream>

using namespace std;

class Ball {
    public:
        static int nBalls;
        string col;
        Ball::Ball(string color) {
            nBalls++;
            col = color;
        }
};

int main() {
    Ball j = Ball("red");
    cout << "Ball " << Ball::nBalls << ": ";
    cout << j.col << endl;
    Ball k = Ball("green");
    cout << "Ball " << Ball::nBalls << ": ";
    cout << k.col << endl;
    return 0;
}
