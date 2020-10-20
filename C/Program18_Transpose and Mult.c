#include<stdio.h>

int main()
 {
 	int a[100][100],m,n,i,j,b[100][100],c[100][100];
 	printf("\n Enter no of rows : ");
 	scanf("%d",&m);
 	printf("\n Enter the no of columns : ");
 	scanf("%d",&n);
 	printf("\nEnter the Matrix : \n");
 	for (i=0;i<m;i++)
 	 {
 	 	for (j=0;j<n;j++)
 	 	 {
 	 	 	scanf("%d",&a[i][j]);
		   }
	  }
	printf("\n The Entered Matrix is :\n");
	for(i=0;i<m;i++)
	 {
	 	for(j=0;j<n;j++)
	 	 {
	 	 	printf("%d ",a[i][j]);
		  }
		printf("\n");
	 }
	for (i=0;i<m;i++)
	 {
	 	for(j=0;j<n;j++)
	 	 {
	 	 	b[j][i]=a[i][j];
		  }
	 }
	printf("\n The Transpose of the Matrix is :\n");
	for(i=0;i<m;i++)
	 {
	 	for(j=0;j<n;j++)
	 	 {
	 	 	printf("%d ",b[i][j]);
		  }
		printf("\n");
	 }
	int k,sum=0;
	for(i=0;i<m;i++)
	 {
	 	for (j=0;j<n;j++)
	 	 {
	 	 	for(k=0;k<n;k++)
	 	 	 {
	 	 	 	sum+=a[i][k]*b[k][j];
			   }
			c[i][j]=sum;
		  }
	 }
	printf("\n The Product Matrix of the above 2 Matrices is :\n");
	for(i=0;i<m;i++)
	 {
	 	for(j=0;j<n;j++)
	 	 {
	 	 	printf("%d     ",c[i][j]);
		  }
		printf("\n");
	 }
 }
