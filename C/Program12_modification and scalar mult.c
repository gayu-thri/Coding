#include<stdio.h>
struct Array
 {
 	int a[100];
 };
 
int main()
 {
 	int m,n,i,j,ele,p,q,num;
 	printf("\n Enter the no of Arrays : ");
 	scanf("%d",&m);
 	printf("\n Enter the size of the Arrays : ");
 	scanf("%d",&n);
 	struct Array x[m];
 	for (i=0;i<m;i++)
 	 {
 	 	printf("\n Enter the Array %d: \n",i+1);
 	 	for (j=0;j<n;j++)
 	 	 scanf("%d",&x[i].a[j]);
 	 	
	  }
	printf("\n Enter the Array number to be Modified : ");
	scanf("%d",&p);
	printf("\n Enter the element position to be modified : ");
	scanf("%d",&q);
	printf("\n Enter the Number to be replaced at the above given position input : ");
	scanf("%d",&num);
	x[p-1].a[q-1] = num;
	printf("\n Enter a Scalar to be Multiplied with the vector : ");
	scanf("%d",&ele);
	for (i=0;i<m;i++)
	 {
	 	for (j=0;j<n;j++)
	 	 {
	 	 	x[i].a[j] = x[i].a[j] * ele;
		  }
	 }
	printf("\n Arrays after Modification and Scalar Multiplication is : \n");
	for (i=0;i<m;i++)
	 {
	 	for (j=0;j<n;j++)
	 	 {
	 	 	printf("%d  ",x[i].a[j]);
		  }
		printf("\n");
	 }
 }
