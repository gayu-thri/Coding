#include<stdio.h>

int main()
 {
 	series();
 }
 
int series()
 {
 	int i,sum=0,f=1;
	for(i=1;i<=5;i++)
 	 {
 	 	f=f*i;
 	 	sum+=(f/i);
	  }
	printf("\n The sum of the series is : %d\n",sum);
 }
