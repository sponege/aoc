#include <stdio.h>

int main() {
	int i = 0;
	for (; i < 1000000000; i++) {}
	printf("%d\n",i);
}
