#include<stdio.h>
int main()
{
int num;
printf("Enter a number:");
scanf("%d",&num);
if(num>=1)
  printf("%d is Positive",num);
else if(num<0)
  printf("%d is Negative",num);
else if(num==0)
  printf("The number is Zero");
else
  printf("INVALID");
return 0;
}
