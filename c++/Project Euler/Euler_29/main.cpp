#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    vector<long> nums;
    nums.push_back((long) 0);
    bool add = true;
    long exp;
    for (int a = 2; a <= 3; a++) {
        for (int b = 2; b <= 3; b++) {
            exp = (long) pow((double) a, (double) b);
            for (int c = 0; c < (int) nums.size(); c++) {
                cout << nums[c] << endl;
                if (nums[c] == exp) {
                    add = false;
                }
            }
            if (add == true) {
                nums.push_back(exp);
            }
            add = true;
        }
    }
    cout << "Terms: " << nums.size() - 1;
}
