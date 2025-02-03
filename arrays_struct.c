#include <stdio.h>
#include <stdlib.h>

int main() {
    typedef struct {
        char name[20];
        int age;

    } Mahasiswa;

    Mahasiswa humblegod = {"Humble God", 20};

    Mahasiswa kelas[5] ={
        {"Humble God", 20},
        {"Naruto", 21},
        {"Sasuke Uchiha", 22},
        {"Shugo Uchiha", 23},
        {"Itachi Uchiha", 24}
    };

    printf("Name: %s\nAge: %d\n", humblegod.name, humblegod.age);
    
    printf("\n\nList Mahasiswa:\n");
    for (int i = 0; i < 5; i++) {
        printf("Name: %s\nAge: %d\n", kelas[i].name, kelas[i].age);
    }

    
    
}