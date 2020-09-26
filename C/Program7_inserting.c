#include<stdio.h>

int insert (int arr[],int s,int p,int e)
 {
 	int i;
 	for (i=s-1;i>=p-1;i--)
 	  arr[i+1]=arr[i];
 	arr[p-1]=e;
 	printf("\n The Final Array is : \n");
 	for (i=0;i<=s;i++)
 	  printf("%d  ",arr[i]);
 }
 
 
int main()
 {
 	int a[100],size,pos,i,ele;
 	printf("\n Enter the no of elements to be inserted in the array : ");
 	scanf("%d",&size);
 	printf("\n Enter the element to be added : ");
 	scanf("%d",&ele);
 	printf("\n Enter the Array : \n");
 	for (i=0;i<size;i++)
 	 {
 	 	scanf("%d",&a[i]);
	  }
	printf("\n The Final Array is : \n");
 	for (i=0;i<size;i++)
 	  printf("%d  ",a[i]);
	printf("\n Enter the Position : ");
	scanf("%d",&pos);
	insert(a,size,pos,ele);
 }
