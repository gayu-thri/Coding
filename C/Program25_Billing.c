#include<stdio.h>
#include<string.h>

struct billing
 {
 	char custname[100],street[50],city[50],state[50],acctype[10];
 	int accnum,prevbal,currpay,newbal,paydate;
 }a[100];
 
int getdata(int x)
 {
 	int i;
 	for(i=0;i<x;i++)
 	 {
 	 	printf("\n Enter Customer name : ");
 	    scanf("%s",a[i].custname);
 	 	printf("\n Enter the customer street : ");
 	 	scanf("%s",a[i].street);
 	 	printf("\n Enter the customer city : ");
 	 	scanf("%s",a[i].city);
 	 	printf("\n Enter the customer state : ");
 	 	scanf("%s",a[i].state);
 	 	printf("\n Enter the account number : ");
 	 	scanf("%d",&a[i].accnum);
 	 	printf("\n Enter the Previous Existing balance : ");
 	 	scanf("%d",&a[i].prevbal);
 	 	printf("\n Enter the Current Payment : ");
 	 	scanf("%d",&a[i].currpay);
 	 	printf("\n Enter the Payment Date : ");
 	 	scanf("%d",&a[i].paydate);
	  }
 }
 
int compare(int x)
 {
 	int i;
 	for(i=0;i<x;i++)
 	 {
 	 	if((a[i].currpay)>0 && (a[i].currpay)<((a[i].prevbal)/10))
 	 	 {
 	 	 	strcpy(a[i].acctype,"Overdue");
		   }
		else if(a[i].prevbal==0 && a[i].currpay==0)
		 {
		 	strcpy(a[i].acctype,"Delinquent");
		 }
		else
		 {
		 	strcpy(a[i].acctype,"Current");
		 }
		a[i].newbal=(a[i].prevbal-a[i].currpay);
	  }
 }
 
int display(int x)
 {
 	int i;
 	for(i=0;i<x;i++)
 	 {
 	 	printf("\n details of Customer %d : \n",i+1);
 	 	printf(" Customer Name : %s",a[i].custname);
 	 	printf("\n Customer Street : %s",a[i].street);
 	 	printf("\n Customer City : %s",a[i].city);
 	 	printf("\n Customer State : %s",a[i].state);
 	 	printf("\n Customer Account Number : %d",a[i].accnum);
 	 	printf("\n Customer Account Type : %s",a[i].acctype);
 	 	printf("\n Customer Previous Balance : %d",a[i].prevbal);
 	 	printf("\n Customer Current Payment : %d",a[i].currpay);
 	 	printf("\n Customer New Balance : %d",a[i].newbal);
 	 	printf("\n Customer Payment Date : %d",a[i].paydate);
	  }
 }
 
int main()
 {
 	int n;
 	printf("\n Enter the total Number of Customers : ");
 	scanf("%d",&n);
 	getdata(n);
 	compare(n);
 	display(n);
 }
