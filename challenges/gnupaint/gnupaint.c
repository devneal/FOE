#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MENU "Main Menu\n1) Print\n2) Pen Tool\n3) Zoom Tool\n4) Rename\n9) Quit\n\nEnter selection: "

#define HEIGHT 10
#define WIDTH 40
#define SIZE HEIGHT*WIDTH
#define COORD(y,x) y*HEIGHT+x
#define ELM_SIZE 32
#define ELEMENT "\x1B[%lum%%s\x1B[0m" // ANSI color codes

char name[64] = "Untitled.bmp";
long int image[SIZE];

// HELPER FUNCTIONS
void update(long int image[], int x, int y, long int z) {
    image[COORD(y,x)] = z;
}

void init(long int image[]) {
    for (int i=0; i < WIDTH*HEIGHT; i++)
        update(image, i, 0, 40+(i%8));
}

// MENU FUNCTIONS
void print_image(long int image[]) {
    char this_elm[ELM_SIZE];

    puts(name);
    for (int i=0; i < WIDTH*HEIGHT; i++) {
        if (i%WIDTH== 0) puts("");
        snprintf(this_elm, ELM_SIZE, ELEMENT, image[i]);
        printf(this_elm, " ");

    }
}

void pen_tool() {
    puts("Pen Menu");
    printf("Enter X coordinate: ");

    int x,y;
    long int val;
    scanf("%d", &x);

    printf("Enter Y coordinate: ");
    scanf("%d", &y);
    if (x > WIDTH || y > HEIGHT) goto no;

    printf("Pen (ANSI) Color: ");
    scanf("%ld", &val);

    char junk[1]; // Consume the newline before going back to menu
    scanf("%c", junk);
    update(image, x, y, val);

    puts("Updated");
    return;
no:
    puts("Invalid coordinate");
}

void zoom_tool() {
    puts("Zoom Menu");
    printf("Enter X coordinate: ");

    int x,y;
    scanf("%d", &x);

    printf("Enter Y coordinate: ");
    scanf("%d", &y);

    char junk[1]; // Consume the newline before going back to menu
    scanf("%c", junk);

    if (x > WIDTH || y > HEIGHT) goto no;
    printf("Pixel (%d, %d) looks like:\n", x, y);

    char this_elm[ELM_SIZE];
    snprintf(this_elm, ELM_SIZE, ELEMENT, image[COORD(y,x)]);
    printf(this_elm, "   \n   ");
    printf("\n");

    return;

no:
    puts("Invalid coordinate");
}

void rename_tool() {
    puts("Rename Menu");
    printf("Entire new name: ");
    char *line = NULL;
    size_t size;
    if (getline(&line, &size, stdin) == -1) {
        puts("Error");
        return;
    }
    strncpy(name, line, 32);
    if (strlen(name) > 0 && strlen(name) < 32)
        name[strlen(name)-1] = 0; // remove newline

    strncat(name, ".bmp\0", 32);
    puts("Drawing renamed");
}

char menu() {
    printf("%s", MENU);

    char *line = NULL;
    size_t size;
    if (getline(&line, &size, stdin) == -1) {
        puts("Error");
        return 1;
    }

    switch (line[0]) {
            break;
        case '1':
            print_image(image);
            break;
        case '2':
            pen_tool();
            break;
        case '3':
            zoom_tool();
            break;
        case '4':
            rename_tool();
            break;
        case '9':
            puts("Goodbye\n");
            return 0; // 0 means quit
            break;
        default:
            printf("Invalid option\n");
            break;
    }

    puts("");
    return 1;
}

int main() {
    init(image);

    printf("Welcome to GNU/Paint!\n");
    while (menu()) {
        system("sleep 0.5");
    }

    return 0;
}
