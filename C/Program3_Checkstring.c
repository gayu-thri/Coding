#include<stdio.h>
int main()
{
	char str[100];
	int vowels,consonants,digits,space;
	vowels=consonants=digits=space=0;
	printf("Enter the string :   \n");
	scanf("%[^\n]s",&str);
    int i=0;
	while(str[i]!='\0')
	   {
	   	  if(str[i]==' ')
	   	      ++space;
	   	      
	   	       else if(str[i]>='0'&&str[i]<='9')
	             	            ++digits;
	   	      
	   	      else if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u'||str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U')
	   	              ++vowels;
	   	              
	             	else if((str[i]>='a'&&str[i]<='z')||(str[i]>='A'&&str[i]<='Z'))
	             	    ++consonants;
	             	    
	             	  
	       i++;      	            
		}	
	
	printf("\n\nThe number of digits in the given string is  : %d\n",digits);
	printf("The number of spaces in the given string is  : %d\n",space);
	printf("The number of vowels in the given string is  : %d\n",vowels);
	printf("The number of consonants in the given string is  : %d\n",consonants);
}
