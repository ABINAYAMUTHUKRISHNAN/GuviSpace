#include<stdio.h>
void main()
{
 int num;
 printf("Enter the size of array:");
 scanf("%d",&num);
 int arr[num];
 int mini=0;
 int maxi=99999;
 for(int j=0;j<num;j++)
 {
   printf("Enter the %d number:",j+1);
   scanf("%d",&arr[j]);
 }
 for(int i=0;i<num;i++)
 {
   if (arr[i]>mini)
     mini=arr[i];
   if (arr[i]<maxi)
     maxi=arr[i];
 }
 printf("Maximum number:%d\nMinimum number:%d",mini,maxi);
}
