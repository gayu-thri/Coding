#include<stdio.h>
#include<string.h>
struct date
{
	int yr;
};
date curr={2018};
struct drugs
{
	int code, ct;
	char name[18];
	date exp;
	void input()
	{
		printf("\nEnter drug code : ");
		scanf("%d", &code);
		printf("\nEnter drug count : ");
		scanf("%d", &ct);
		printf("\nEnter drug name : ");
		scanf("%s", &name);
		printf("\nEnter expiry year : ");
		scanf("%d", &exp.yr);
	}
	void output()
	{
		printf("\n Drug code : ");
		printf("%d\n", code);
		printf("\n Drug count : ");
		printf("%d\n", ct);
		printf("\n Drug name : ");
		printf("%s\n", name);
		printf("\n Expiry date : ");
		printf("%d\n\n", exp.yr);
	}
	void assign(drugs a)
	{
		code=a.code;
		ct=a.ct;
		strcpy(name,a.name);
		exp.yr=a.exp.yr;
	}
	void del()
	{
		char temp[]="\n";
		code=ct=exp.yr=0;
		strcpy(name,temp);
	}
};
int exp_drugs(drugs stock[], drugs exp[], int &n, int &m)
{
	int counter=0, i;
	for(i=0;i<n;i++)
	{
		if(stock[i].exp.yr<curr.yr)
		{
			exp[m++].assign(stock[i]);
			stock[i].del();
			counter++;
		}
	}
	return(counter);
}
int main()
{
	drugs a[108], b[108];
	int n, i, m=0;
	printf("\n Enter number of records required : ");
	scanf("%d", &n);
	printf("\n Enter the records one by one...\n");
	for(i=0;i<n;i++)
	a[i].input();
	printf("\n Enter current date:-");
	scanf("%d", &curr.yr);
	printf("\nThe number of drugs expired are:-");
	printf("%d", exp_drugs(a,b,n,m));
	printf("\nThe final stock is...\n");
	for(i=0;i<n;i++)
	a[i].output();
	printf("\nThe final expired drugs are...");
	for(i=0;i<m;i++)
	b[i].output();
	return 0;
}
