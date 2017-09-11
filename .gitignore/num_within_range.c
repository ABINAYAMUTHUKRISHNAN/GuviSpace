#include<stdio.h>
void main()
{
  int num;
  printf("Enter a number:");
  scanf("%d",&num);
  if ((num>=1)&&(num<=9))
   printf("%d",num);
  else
   printf("you entered number is not in range");
}
