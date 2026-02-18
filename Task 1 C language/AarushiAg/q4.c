#include <stdio.h>

int main() {
    int n1, n2;
    int a[100], b[100];
    int inter[100], uni[200];
    int icount = 0, ucount = 0 , i, j, found;

    printf("Enter number of elements for array A: ");
    scanf("%d", &n1);

    for (i = 0; i < n1; i++)
        scanf("%d", &a[i]);

    printf("Enter number of elements for array B: ");
    scanf("%d", &n2);

    for (i = 0; i < n2; i++){
        scanf("%d", &b[i]);}

    for (i = 0; i < n1; i++) {
        for (j = 0; j < n2; j++) {
            if (a[i] == b[j]) {
                inter[icount++] = a[i];
                break;}}}

    for (i = 0; i < n1; i++){
        uni[ucount++] = a[i];}

    for (i = 0; i < n2; i++) {
        found = 0;
        for (j = 0; j < n1; j++) {
            if (b[i] == a[j]) {
                found = 1;
                break;}}
        if (!found)
            uni[ucount++] = b[i]}

    printf("Intersection: ");
    for (i = 0; i < icount; i++)
        printf("%d ", inter[i]);

    printf("\nUnion: ");
    for (i = 0; i < ucount; i++){
        printf("%d ", uni[i]);}
    return 0;}
