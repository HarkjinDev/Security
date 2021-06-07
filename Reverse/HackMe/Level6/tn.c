// This is the restore code of tn.s

#include <stdio.h>
#include <signal.h>

void sig_func(int signo)
{
        printf("Can't use ctrl+c\n");
}

int main()
{
        char input;
        int select, i;

        system("cat hint");
        input = getchar();
        system("clear");

        printf("#####################################\n");
        printf("##                                 ##\n");
        printf("##        텔넷 접속 서비스         ##\n");
        printf("##                                 ##\n");
        printf("##     1. 하이텔   2. 나우누리     ##\n");
        printf("##     3. 천리안                   ##\n");
        printf("##                                 ##\n");
        printf("#####################################\n");

        for(i=1; i<32; i++)
        {
                if(i == SIGINT) signal(i, sig_func);
                else signal(i, SIG_IGN);
        }

        printf("\n접속하고 싶은 bbs를 선택하세요 : ");
        switch(input)
        {
                case 1: system("telnet 203.245.15.76"); break;
                case 2: system("telnet 203.238.129.97"); break;
                case 3: system("telnet 210.120.128.180"); break;
                default:
                        if(input !=1 && input !=2 && input !=3)
                                printf("잘못 입력하셨습니다. 접속을 종료합니다.\n");
        }
        return 0;
}
