# This is the editor.s of restore code

#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	setreuid(3003, 3003);
	system("/bin/vi");
}
