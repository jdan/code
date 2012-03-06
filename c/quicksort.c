#include <stdio.h>

void quicksort(int *a, int n) {
  if (n == 0)
    return;

  int i, c, r = n-1, len;
  int *temp = (int*)malloc(n * sizeof(int));

  for (i = 1, c = 0; i < n; i++) {
    if (a[i] < a[0])
      temp[c++] = a[i];
    else if (a[i] >= a[0])
      temp[r--] = a[i];
  }

  len = c;
  temp[c++] = a[0];

  for (i = 0; i < n; i++)
    a[i] = temp[i];

  quicksort(a, len);
  quicksort(a + len + 1, n - len - 1);
}

int main (int argc, char **argv) {
  int i, k;
  int *nums = (int*)malloc((argc - 1) * sizeof(int));

  for (i = 1; i < argc; i++)
    nums[i-1] = atoi(argv[i]);

  quicksort(nums, argc-1);

  for (k = 0; k < argc-1; k++)
    printf("%d ", nums[k]);
  printf("\n");

  return 0;
}
