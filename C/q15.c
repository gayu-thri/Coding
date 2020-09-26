#include<stdio.h>
int n,i=0;
struct book
{
	long int accno;
	char title[50];
	int price;
	struct date
	{
		int month;
		int year;
	}dt;
	char publication[50];
}bk[50];

void get_data()
{
	int flg;
	printf("Enter the no. of books:");
	scanf("%d",&n);
	
	for(;i<n;i++)
	{
		flg=1;
		printf("Enter the Book's accno.:");
		scanf("%d",&bk[i].accno);
		printf("Enter the Title of the book:");
		scanf("%s",bk[i].title);
		printf("Enter the price of the Book:");
		scanf("%d",&bk[i].price);
		while(flg)
		{
			printf("Enter the month(mm) and the year(yyyy) publication :");
			scanf("%d",&bk[i].dt.month);
			scanf("%d",&bk[i].dt.year);
			if((bk[i].dt.month>0 && bk[i].dt.month<13) && ( bk[i].dt.year>0))
				flg=0;
			else
				printf("you have entered invalid month and year!!!");
		}
		printf("Enter the Publication name:");
		scanf("%s",bk[i].publication);
	}
}

struct book *search(long int num)
{
	struct book *p;
	p=bk;
	for(i=0;i<n;i++)
	{
		if(num == (*p).accno)
			break;
		else
			p++;
	}
	if(i<n)
		return p;
	else
		printf("Book not found in the record!!!");
}
void disp(int num)
{
	printf("Books published on the year %d are:-\n",num);
	for(i=0;i<n;i++)
	{
		if(bk[i].dt.year == num)
			printf("->%s\n",bk[i].title);
	}
}
void main()
{
	
	get_data();
	int flg=1;
	int ch;
	long int num;
	struct book *sb=NULL;
	while(flg)
	{
		printf("\t\t\tMenu:-\n1)search\n2)list of books published in a particular year\n");
		scanf(" %d",&ch);
		if(ch == 1)
		{
			printf("Enter the accno of the book to be searched: ");
			scanf("&d",&num);
			sb=search(num);
			if(sb != NULL)
			{
				printf("Book's accno.:%d\n",(*sb).accno);
				printf("Title of the book:%s\n",(*sb).title);
				printf("Price of the Book:%d\n",(*sb).price);
				printf("Published Date of the Book (mm/yyyy):%d//%d\n",(*sb).dt.month,(*sb).dt.year);
				printf("publication:%s\n",(*sb).publication);
			}
		}
		else if(ch==2)
		{
			printf("Enter the Year (yyyy):");
			scanf("&d",&num);
			disp(num);
		}
		else
			printf("You have entered the wrong option!!!!");
		printf("Do You want to try again(1-Yes/any key-NO");
		scanf("&d",&ch);
		if(ch!=1)
		{
			printf("\t\t\tThank You !!!");
			flg=0;
		}
			
	}
}
