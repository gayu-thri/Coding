#include<stdio.h>

int power(int m,int n)
 {
 	int result,i;
	if(n==0)
 	 {
 	 	result=m*m;
	  }
	else
	 {
	 	result=1;
	 	for (i=0;i<n;i++)
	 	 {
	 	 	result*=m;
		  }
	 }
	return result;
 }
 
int main()
 {
 	double a;
 	int b,result;
 	do
 	 {
 	 	printf("\n Enter the base number : ");
 	 	scanf("%lf",&a);
 	 	printf("\n Enter the exponential number : ");
 	 	scanf("%d",&b);
	  }while(a==0 && b==0);
	result = power(a,b);
	if(b==0)
	 {
	 	printf("\n As you entered exponential number as 0\nThe square of %.1lf is %d",a,result);
	 }
	else
	 {
	 	printf("\n %.1lf to the power of %d is : %d\n",a,b,result);
	 }
 }
