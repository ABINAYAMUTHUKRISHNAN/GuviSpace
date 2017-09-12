#include<stdio.h>
void main()
{
  int num,count=0;
  printf("Enter the size of the array:");
  scanf("%d",&num);
  int arr[num];
  for(int i=0;i<num;i++)
  {
   printf("Enter the %d number:",i+1);
   scanf("%d",&arr[i]);
  }
  for(int j=0;j<num;j++)
  {
    count+=arr[j];
  }
  printf("Average is:%d",count/num);
}
