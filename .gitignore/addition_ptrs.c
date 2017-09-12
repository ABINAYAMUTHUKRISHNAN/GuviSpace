#include<stdio.h>
void main()
{
  int num1,num2,*p1,*p2;
  printf("Enter two numbers:");
  scanf("%d%d",&num1,&num2);
  p1=&num1;
  p2=&num2;
  if ((num1>=1) && (num2>=1))
    printf("Sum is %d",*p1+*p2);
  else
    printf("Invalid");
}
