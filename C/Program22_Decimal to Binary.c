#include<stdio.h>

int main()
 {
 	int num;
 	printf("\n Enter a Number : ");
 	scanf("%d",&num);
 	convert(num);
 }
 
int convert(int dec)
 {
 	int i=0,bin[100],j;
 	while(dec>0)
 	{
 		bin[i]=dec%2;
 		dec=dec/2;
 		i++;
	 }
	printf("\n Binary Equivalent is \n");
	for(j=i-1;j>=0;j--)
	{
		printf("%d",bin[j]);
	}
 }
