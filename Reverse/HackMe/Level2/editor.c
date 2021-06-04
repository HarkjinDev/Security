# This is the restore code of editor.s

#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	setreuid(3003, 3003);
	system("/bin/vi");
}
