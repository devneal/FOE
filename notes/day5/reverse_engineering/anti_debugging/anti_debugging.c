#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ptrace.h>

unsigned char s[] = "flag{runn4bl3_m34n5_d3bu664bl3}";
unsigned char expected_result[] = { 0x66, 0xd6, 0x36, 0xa6, 0xf7,
                                    0x77, 0xb7, 0x57, 0x67, 0xd3,
                                    0xc6, 0x77, 0xf3, 0xc6, 0xb7,
                                    0x24, 0x44, 0xf7, 0x74, 0x27,
                                    0x87, 0x84, 0x87, 0xc8, 0xe4,
                                    0xf4, 0xe4, 0xd7, 0x88, 0x05,
                                    0xb9, 0x00 };

unsigned char swapnibbles(unsigned char c) {
    return ((c & 0xF0) >> 4) | ((c & 0x0F) << 4);
}

//int main(void) {
//    if (ptrace(PTRACE_TRACEME, 0, NULL, 0) == -1) {
//        printf("no debuggers allowed!\n");
//        exit(0);
//    }
//
//    int len = strlen((char*)s);
//
//    for (int i=0; i<len; i++)
//        s[i] += i;
//
//    for (int i=0; i<len; i++)
//        s[i] = swapnibbles(s[i]);
//
//    for (int i=0; i<len; i++)
//        printf("%02x ", s[i]);
//
//    return 0;
//}

int main(void) {
    if (ptrace(PTRACE_TRACEME, 0, NULL, 0) == -1) {
        printf("no debuggers allowed!\n");
        exit(0);
    }

    unsigned char input[32];
    scanf("%31s", input);

    int len = strlen((char *)expected_result);

    for (int i=0; i<len; i++)
        expected_result[i] = swapnibbles(expected_result[i]);

    for (int i=0; i<len; i++)
        expected_result[i] -= i;

    if (strcmp((char *)input, (char *)expected_result) == 0)
        printf("Congratulations!!!\n");
    else
        printf("Try again...\n");

    return 0;
}
