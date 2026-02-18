#include <stdio.h>
int main() {
    int rows = 5;
    int curr = 0;
    while (curr < rows) {
        int spaces = rows - curr - 1;
        int tstars  = curr + 1;
        int s = 0;
        while (s < tspaces) {
            printf("  ");
            s++; }
        int k = 0;
        while (k < tstars) {
            printf("* ");
            k++;  }
        printf("\n");
        curr++;}
    return 0;}
