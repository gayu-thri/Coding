#include<stdio.h>
#include<string.h>

struct date
{
	int mon, yr;
};

const date curr={5,2018};

struct book
{
	int accno, price;
	char title[18];
	date pub;
	void input()
	{
		printf("\n Enter the account number : ");
		scanf("%d", &accno);
		printf("\n Enter the price : ");
		scanf("%d", &price);
		printf("\n Enter the title : ");
	    scanf("%s", &title);
		printf("\n Enter the month of publication : ");
		scanf("%d", &pub.mon);
		printf("\n Enter the year of publication : ");
		scanf("%d", &pub.yr);
	}
	
	void output()
	{
		printf("\n Account number : ");
		printf("%d",accno);
		printf("\n Price : ");
		printf("%d", price);
		printf("\n Title : ");
		printf(title);
		printf("\n Month of publication : ");
		printf("%d", pub.mon);
		printf("\n Year of publication : ");
		printf("%d", pub.yr);
	}
};

int cmp(book a, book b)
{
	int flag=0;
	if(a.accno!=b.accno)
	flag++;
	if(a.price!=b.price)
	flag++;
	if(strcmp(a.title,b.title))
	flag++;
	if(a.pub.mon!=b.pub.mon)
	flag++;
	if(a.pub.yr!=b.pub.yr)
	flag++;
	return(flag);
}

book* search(book a[], book &ele, int &n)
{
	book *ptr;
	int i;
	for(i=0;i<n;i++)
	{
		if(!cmp(a[i],ele))
		ptr=&a[i];
	}
	return(ptr);
}

void display(book a[], int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(a[i].pub.yr==curr.yr)
		a[i].output();
	}
}

int main()
{
	book a[108], ele, *ans;
	int n, i;
	printf("\n Enter number of books required : ");
	scanf("%d", &n);
	printf("\n Enter the book details : \n");
	for(i=0;i<n;i++)
	a[i].input();
	printf("\n Enter the book to be searched : \n");
	ele.input();
	ans=search(a,ele,n);
	(*ans).output();
	printf("\n Books published in this year are : \n");
	display(a,n);
	return 0;
}
