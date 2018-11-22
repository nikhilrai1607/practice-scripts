#include <stdio.h>

int main(){

    char x[3];
    int y;
    //Simple print
    printf("welcome to the C language\n");
    //Using Puts function
    puts("this something to test puts() function\n");
    //Using escaped characters
    puts("Hello this is an \"Escaped character\" hahaha\n");

    //Using place holders like %d,%s in PRINTF function
    printf("Hi my name is %s and I am %d years old.","Nikhil",27);

    //Use scanf and assign it to the variable x
    scanf("%s",x);

    //Anything other than a string or array will need '&' to assign the input to the variable
    scanf("%d",&y);
    printf("%s\n",x);
    printf("%d \n",y);
    return(0);
}
