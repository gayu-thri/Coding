#include<stdio.h>

int main()
 {
 	int m,n,i,j,a[100][100],sum=0;
 	printf("\n Enter the number of rows of the matrix : ");
 	scanf ("%d",&m);
 	printf("\n Enter the number of columns of the Matrix : ");
 	scanf("%d",&n);
 	printf("\n Enter the Matrix : \n");
 	for (i=0;i<m;i++)
 	 {
 	 	for (j=0;j<n;j++)
 	 	 {
 	 	 	scanf("%d",(*(a+i)+j));
		   }
	  }
	for (i=0;i<m;i++)
	 {
	 	sum=0;
		for (j=0;j<n;j++)
	 	 {
	 	 	sum+=*(*(a+i)+j);
		  }
		printf("\n Sum of Row %d is : %d ",i+1,sum);
	 }
 }
