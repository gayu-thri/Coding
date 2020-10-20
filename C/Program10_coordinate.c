#include<stdio.h>

struct coordinate
 {
 	float x;
 	float y;
 }point;
 
int main()
 {
 	printf("\n Enter X coordinate : ");
 	scanf("%f",&point.x);
 	printf("\n Enter Y coordinate : ");
 	scanf("%f",&point.y);
 	if ((point.x > 0)&&(point.y > 0))
 	 printf("\n I Quadrant\n");
 	if ((point.x < 0)&&(point.y > 0))
 	 printf("\n II Quadrant\n");
 	if ((point.x < 0)&&(point.y < 0))
 	 printf("\n III Quadrant\n");
 	if ((point.x > 0)&&(point.y < 0))
 	 printf("\n IV Quadrant\n");
 }
