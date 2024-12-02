#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <signal.h>

#define numlines 100
#define maxlinelen 100

int main() {
	char**lines = malloc(numlines*sizeof(char*));
	int lc = 0; // line count
	for(;lc<numlines;lc++) {
		lines[lc] = malloc(maxlinelen*sizeof(char));
		// read one line
		int c = 0;
		int eof = 0;
		for(;c<maxlinelen;c++) {
			char ch = getchar();
			if (ch == EOF) {
				eof = 1;
				break;
			}
			if (ch == '\n') {
				break;
			}
			lines[lc][c] = ch;
		}
		if (eof) {
			break;
		}
	}

	puts("-------\n");

	for(int i=0;i<lc;i++) {
		printf("%s",lines[i]);
	}
	printf("Number of lines: %d\n",lc);
}
