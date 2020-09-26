#include<stdio.h>

int main()
 {
 	int num,sum;
 	printf("\n Enter a Number : ");
 	scanf("%d",&num);
 	sum=total(num);
 	printf("\n The Total is : %d \n",sum);
 }
 
int total(int n)
 {
 	static int sum=0;
 	if(n>0)
 	 {
 	 	sum+=(n%10);
 	 	total(n/10);
	  }
	else
	 return sum;
 }
