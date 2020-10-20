#include<stdio.h>

int main()
 {
 	int end;
 	printf("\n Enter the end limit : ");
 	scanf("%d",&end);
 	perfect(end);
 }
 
int perfect(int num)
 {
 	int i,j,sum;
 	printf("\n All Perfect numbers from 1 to %d are : \n",num);
 	for(i=1;i<=num;i++)
 	 {
 	 	sum=0;
		for (j=1;j<i;j++)
 	 	 {
 	 	 	if(i%j==0)
 	 	 	 {
 	 	 	 	sum+=j;
				}
		   }
		if (sum==i)
		 {
		 	printf("\n %d ",i);
		 }
	  }
 }
