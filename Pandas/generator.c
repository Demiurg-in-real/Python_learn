#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
void main(){
	FILE *smth=fopen("test.txt","w");
	if(smth == NULL){
		printf("Smth goes wrong!\n");
		abort();
	}
	int simv;
	int i=256;
	time_t lt;
	srand(time(&lt));
	simv=rand();
	while (i--){
		do{
			simv=rand();
		}
		while((simv<=122 && simv>=65) || (simv>=48 && simv<=57) || (simv == 0x20));
		fputc(simv,smth);
		//fwrite(&simv, sizeof(char), 1,smth);
		if( (i%16) == 0) printf("%d", lt);
	}
	fclose(smth);
}
