#include<stdio.h>

int main()
 {
 	int num,a[100],i,j=0;
 	printf("\n Enter a number : ");
 	scanf("%d",&num);
 	for (i=1;i<num/2;i++)
 	 {
 	 	if((num%i)==0)
 	 	 {
 	 	 	a[j]=i;
 	 	 	j++;
		   }
	  }
	printf("\n The Factors are : \n");
	for (i=0;i<j;i++)
	 {
	 	printf("\n %d ",a[i]);
	 }
 }
