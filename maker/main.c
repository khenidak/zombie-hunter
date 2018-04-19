#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main ()
{
	#define MAX_ZOMBIE 1000
	pid_t pid_zombie;
	pid_t me;

	for(int n = 0; n< MAX_ZOMBIE; n++)
	{
		me = getpid();
		pid_zombie = fork();
		if (pid_zombie > 0) {
			printf("[%d] created a zombie with pid:%d \n", me, pid_zombie);
			sleep(1);
		} else {
			me = getpid();
			printf("[%d] is about to become a zombie ... GRRRR! \n", me);
			exit(0);
		}
	}
    // after 2 min, we exit, init/systemd will reap it.
    sleep(120);
	return 0;
}
