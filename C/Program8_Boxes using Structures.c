#include<stdio.h>

struct box
 {
 	float len;
 	float breadth;
 	float height;
 	float volume;
 };
 
 int main ()
  {
  	int n,i,j;
  	float temp;
  	printf("\n Enter the Total no of boxes : ");
  	scanf("%d",&n);
  	struct box x[n],vol[n];
  	printf("\nEnter the Dimensions of each box : \n");
  	for (i=0;i<n;i++)
  	 {
  	 	printf("\nLength :  ");
  	 	scanf("%f",&x[i].len);
  	 	printf("\nBreadth :  ");
  	 	scanf("%f",&x[i].breadth);
  	 	printf("\nHeight :  ");
  	 	scanf("%f",&x[i].height);
	   }
	for (i=0;i<n;i++)
	 {
	 	vol[i].volume=((x[i].len)*(x[i].breadth)*(x[i].height));
	printf("\nvolume of box %d : %f\n",i+1,vol[i].volume);
     }
	printf("\nVolumes of the entered no of boxes without arrangement are : \n");
	for(i=0;i<n;i++)
	 {
	 	printf("Box %d : %.2f cubic metres\n",i+1,vol[i].volume);
	 }
	printf("\nVolumes of the entered no of boxes After arrangement are : \n");
	for(i=0;i<n-1;i++)
	 {
	 	for(j=0;j<n-i-1;j++)
	 	 {
	 	 	if(vol[j].volume>vol[j+1].volume)
	 	 	 {
	 	 	 	temp=vol[j].volume;
	 	 	 	vol[j].volume=vol[j+1].volume;
	 	 	 	vol[j+1].volume=temp;
			   }
		  }
	 }
	for(i=0;i<n;i++)
	 {
	 	printf("Box %d : %.2f cubic metres\n",i+1,vol[i].volume);
	 }
  }
