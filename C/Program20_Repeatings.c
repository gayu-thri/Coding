#include<stdio.h>

int main()
 {
 	char str[100];
 	int len,i,words=1,j;
 	printf("\n Enter a String : ");
 	scanf("%[^\n]s",&str);
 	printf("\n The Array is : ");
 	len=printf("%s\n",str);
 	printf("The String Length is : %d \n",len);
 	printf(" The Elements in the String are : \n");
 	/*for (i=0;i<len;i++)
 	 {
 	 	printf("%s ",b[i]);
	  }*/
	printf("%s ",str);
	int f;
	for (i=0;i<len;i++)
	 {
	 	if((str[i+1]==' ')&&(str[i]!=' '))
	 	 words++;
	 }
	printf("\n The no of Words are : %d \n",words);
	printf("The Highest Frequency Element of the String is : \n");
	/*char d[100],cnt[100]={0};
	j=0;
	for (i=0;i<len;i++)
	 {
	 	if(i==0)
	 	 {
	 	 	d[j++]=b[i];
	 	 	cnt[j-1]++;
		  }
		else
		 {
		 	for(k=0;k<j;k++)
		 	 {
		 	 	if(b[i]==d[k])
		 	 	 {
		 	 	 	cnt[k]++;
		 	 	 	f=1;
				   }
			  }
			if (f==0)
			 {
			 	d[j++]=b[i];
			 	cnt[j-1]++;
			 }
			f=0;
		 }
	 }
	for(i=0;i<j;i++)
	 {
	 	if((i==0)&&(d[i]!=' '))
	 	 {
	 	 	max=cnt[i];
	 	 	continue;
		  }
		if((max<cnt[i])&&(d[i]!=' '))
		 {
		 	max=cnt[i];
		 	index=i;
		 }
	 }
	printf("\n Maximum Repeated Character is : %c \n",d[index]);
	printf(" Occured %d Times \n",cnt[index]);*/
	int count[256]={0},max=0;
	char *ptr,m;
	ptr=str;
	if(NULL==ptr)
	 return 0;
	while(*ptr)
	{
		if(++count[*ptr]>max && *ptr!=' ')
		{
		max=count[*ptr];
		m=*ptr;
	}
	 ptr++;
    }
	printf("The most repeated character is :  %c",m);
	
 }
