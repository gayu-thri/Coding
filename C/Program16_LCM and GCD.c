#include<stdio.h>

void lcm_gcd(int,int,int*,int*);

int main()
 {
 	int num1,num2;
 	printf("\n Enter Number 1 : ");
 	scanf("%d",&num1);
 	printf("\n Enter Number 2 : ");
 	scanf("%d",&num2);
 	lcm_gcd(num1,num2,&num1,&num2);
 }

void lcm_gcd(int a,int b,int *x,int *y)
 {
 	int min;
 	if (a>b)
 	 min=a;
 	else 
 	 min=b;
 	while(1)
 	 {
 	 	if (((min%a)==0)&&((min%b)==0))
 	 	 {
 	 	 	printf("\n LCM is : %d",min);
 	 	 	break;
		   }
		++min;
	  }
	int i,gcd;
	for (i=1;(i<=*x)&&(i<=*y);i++)
	 {
	 	if(((*x%i)==0)&&((*y%i)==0))
	 	 gcd=i;
	 }
	printf("\n GCD is : %d \n",gcd);
 }
