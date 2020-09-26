#include<stdio.h>

int main()
 {
 	int i,sum=0,n;
 	int *ptr;
 	printf("\n Enter the Array size : ");
 	scanf("%d",&n);
 	int a[n];
 	printf("\n Enter the Array Elements : \n");
 	for (i=0;i<n;i++)
 	 scanf("%d",&a[i]);
 	ptr=a;
 	for(i=0;i<n;i++)
 	 {
 	 	sum+=*ptr;
 	 	ptr++;
	  }
	printf("\nSum= %d \n",sum);
 }
