#include <iostream>
#include <dos.h>
#include <windows.h>

int main() {
  Sleep(5000);
  for (int i = 0; i < 3000; i++) {
    mouse_event(2,0,0,0,0);
    mouse_event(4,0,0,0,0);
  }
}
