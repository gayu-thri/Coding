#include<stdio.h>
struct employee
{
	int ID;
	float salary;
	char name[20];
};
void salaryraise(struct employee *emp);
int main()
{
	struct employee e={22322,15000,"Rahul"};
	printf("The employee ID  :%d\n",e.ID);
	printf("Employee's Salary  : %f\n",e.salary);
	printf("Employee Name  :");
	puts(e.name);
	printf("\n\t---AFTER RAISE IN SALARY--\n");
	salaryraise(&e);
    printf("The employee ID  :%d\n",e.ID);
	printf("Employee's Salary  :%f\n",e.salary);
	printf("Employee Name  :");
	puts(e.name);
return 0;	
}
void salaryraise(struct employee *emp)
{
	emp->salary+=(0.1*emp->salary);
}
