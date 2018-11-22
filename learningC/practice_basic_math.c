#include <stdio.h>
#include <math.h>
//#include <stdlib.h> used to use rand() function to generate 
int main(){
  //float sq;
  //float po;
  int inp;

  printf("Enter a number to be processed: ");
  scanf("%d",&inp);
  printf("Square root of the number %d: %f",inp,sqrt(inp));
  printf("%d to the power 5: %f",inp,pow(inp,5));

  return(0);
}
