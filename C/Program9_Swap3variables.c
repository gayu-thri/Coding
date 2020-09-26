#include<stdio.h>
void cyclicswap(int *a,int *b,int *c);
int main()
{
	int a,b,c;
	printf("Enter the values of a , b and c respectively :");
	scanf("%d %d %d",&a,&b,&c);
	  printf("\nValues BEFORE SWAPPING   :\n");
	  printf("a = %d \nb = %d \nc =%d",a,b,c);
	  
	cyclicswap(&a,&b,&c);
	  
	  printf("\n\nValues AFTER SWAPPING   :\n");
	  printf("a = %d \nb = %d \nc =%d",a,b,c);
	  
return 0;	   
}
void cyclicswap(int *a,int *b,int *c)
{
	int temp ;

          temp=*b;
          *b=*a;
          *a=*c;
          *c=temp;
}
