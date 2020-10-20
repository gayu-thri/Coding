#include<stdio.h>

int main()
 {
 	int a[100],b[100],n,i,j,ctr;
 	printf("\n Enter the number of Elements : ");
 	scanf("%d",&n);
 	printf("\n Enter the Array Elements : \n");
 	for (i=0;i<n;i++)
 	 {
 	 	scanf("%d",&a[i]);
 	 	b[i]=-1;
	  }
 	for (i=0;i<n;i++)
 	 {
 	 	ctr=1;
 	 	for (j=i+1;j<n;j++)
 	 	 {
 	 	 	if(a[i]==a[j])
 	 	 	 {
 	 	 	 	ctr++;
 	 	 	 	b[j]=0;
				}
		   }
		if (b[i]!=0)
		 b[i]=ctr;
	  }
	printf("\n The Frequency of all Elements are : \n");
	for (i=0;i<n;i++)
	 {
	 	if(b[i]!=0)
	 	 printf("\n %d occurs %d times \n",a[i],b[i]);
	 }
	for (i=0;i<n;i++)
	 {
	 	 	if(b[j]>1)
	 	 	 {
	 	 	 	printf("\n Duplicate Element is : %d \n",a[i]);
			   }
		  
	 }
	printf("\n The Unique Elements are : \n");
	for (i=0;i<n;i++)
	 {
	 	if(b[i]==1)
	 	 {
	 	 	printf("%d \n",a[i]);
		  }
	 }
	return 0;
 }
