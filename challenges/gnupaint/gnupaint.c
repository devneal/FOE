#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Options - you probably want to leave them both off
//#define EXPERT "%lu%%s" // When defined you can print colors as numbers via menu option 0
//#define LOAD // Leaky function to dereference a pointer and print the value

#define MENU "Main Menu\n1) Print\n2) Pen Tool\n3) Zoom Tool\n4) Rename\n9) Quit\n\nEnter selection: "

#define HEIGHT 10
#define WIDTH 40
#define SIZE HEIGHT*WIDTH
#define COORD(y,x) y*HEIGHT+x
#define ELM_SIZE 32
#define ELEMENT "\x1B[%lum%%s\x1B[0m" // Lekas are printed in this form so the terminal gets funky

char name[64] = "Untitled.bmp";
long int image[SIZE];

#ifdef EXPERT
char is_expert = 0; // TODO switch back to 0 for prod
#endif

// HELPER FUNCTIONS
void update(long int image[], int x, int y, long int z) {
    //printf("Write 0x%x to image[%d]\n", z, COORD(y,x));
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
#ifdef EXPERT
        snprintf(this_elm, ELM_SIZE, (is_expert ? EXPERT: ELEMENT), image[i]);
#else
        snprintf(this_elm, ELM_SIZE, ELEMENT, image[i]);
#endif
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
#ifdef EXPERT
    snprintf(this_elm, ELM_SIZE, (is_expert ? EXPERT: ELEMENT), image[COORD(y,x)]);
#else
    snprintf(this_elm, ELM_SIZE, ELEMENT, image[COORD(y,x)]);
#endif
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

#ifdef LOAD
char loaded = 0;
void load_menu() {
    if (loaded) { // Just one load allowed
        puts("You can only load one file!");
        return;
    }
    loaded=1;
    puts("Load menu");
    printf("Address [base 10]: ");
    long x;
    scanf("%ld", &x);

    long object[100];
    memcpy(object, (void*)x, 100);

    if (object[0] != 0x4942813981828382) {
        printf("Invalid object loaded (Signautre mismatch, got %lu)\n", object[0]);
    }else{
        puts("error loading");
    }

    printf("Read object at 0x%X, first byte is 0x%X", x, *object);
}
#endif

char menu() {
    printf("%s", MENU);

    char *line = NULL;
    size_t size;
    if (getline(&line, &size, stdin) == -1) {
        puts("Error");
        return 1;
    }

    switch (line[0]) {
#ifdef EXPERT
        case '0':
            is_expert = !is_expert;
            if (is_expert) {
                puts("Expert mode enabled\n");
            } else {
                puts("Expert mode disabled\n");
            }
#endif
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
#ifdef LOAD
        case '5':
            load_menu();
            break;
#endif
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
