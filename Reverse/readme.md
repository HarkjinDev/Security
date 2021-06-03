# Reverse
## 시스템 CPU 구조

![CPUStructure](/Reverse/CPUStructure.png)


## 연산 장치(ALU:Arithmetic and Logic Unit)

- CPU의 핵심 부분 중 하나로, 산술과 논리 연산을 수행하는 연산 회로 집합으로 구성
- 가산기(Adder) : 덧셈 연산 수행
- 보수기(Complementer) : 뺄셈 연산 수행. 1의 보수나 2의 보수 방식 이용
- 시프터(Shifter) : 비트를 오른쪽이나 왼쪽으로 이동하여 나눗셈과 곱셈 연산 수행
- 누산기(Accumulator) : 연산의 중간 결과 저장
- 데이터 레지스터(Data Register) : 연산에 사용할 데이터 저장
- 상태 레지스터(Status Register) : 연산 실행 결과로 나타나는 양수와 음수, 자리 올림, 오버플로우의 상태 기억



## 제어 장치(Control Unit)

- 입력, 출력, 기억, 연산 장치를 제어하고 감시, 주기억장치에 저장된 명령을 차례로 해독하여 연산 장치로 보내 처리되도록 지시
- 명령 해독기(Instruction Decoder) : 명령 레지스터에 있는 명령을 해독하여 부호기로 전송
- 부호기(Decoder) : 명령 해독기가 전송한 명령을 신호로 만들어 각 장치에 전송
- 주소 해독기(Address Decoder) : 명령 레지스터에 있는 주소를 해독하여 메모리의 실제 주소로 변환한 후, 이를 데이터 레지스터에 저장
- 프로그램 카운터(Program Counter) : 다음에 실핼할 명령의 주소를 저장
- 명령(Instruction) 레지스터 : 현재 실행 중인 명령 저장
- 메모리 주소(Memory Address) 레지스터 : 주기억 장치의 번지 저장
- 메모리 버퍼(Memory Buffer) 레지스터 : 메모리 주소 레지스터에 저장된 주소의 실제 내용 저장



## 레지스터(Register)

- 처리 중인 데이터나 처리 결과를 임시 보관하는 CPU 내의 기억 장치
- 범용레지스터(General-Purpose Registers) : 연산 장치가 수행한 계산 결과의 임시 저장, 산술 및 논리 연산, 주소 색인 등의 목적으로 사용될 수 있는 레지스터 
  + EAX(Accmulator, 누산기) : 모든 연산 명령에 사용되는 레지스터, 산술연산, 입출력, Translate 명령어, 주로 산술 연산에 사용(함수의 결과값 저장)
  + EBX(Base Register, 베이스 레지스터) : 임의의 번지 지정에 사용되는 어드레스 레지스터, offset, 특정 주소 저장(주소 지정을 확대하기 위한 인덱스로 사용)
  + ECX(Counter Register, 카운트 레지스터) : 스트링 조작 명령이나 반복 루프의 계수기로 사용, 반복적으로 실행되는 특정 명령에 사용(루프의 반복 횟수나 좌우 방향 시프트 비트 수 기억)
  + EDX(Data Register, 데이터 레지스터) : 산술연산, EAX와 함께 자주 사용, 일반 자료 저장(입출력 동작에 사용)
- 세그먼트 레지스터(Segment Registers) : 프로그램에 정의된 메모리상의 특정 영역, 코드, 데이터, 스택 등을 포함 
  + CS(Code Segment Register) : DOS의 프로그램 코드 세그먼트의 시작 번지 저장, 이 번지에 명령어 포인터(IP) 레지스터 내의 옵션값을 더하면 실행을 위한 명령어의 번지가 된다.
  + DS(Data Segment Register) : 프로그램의 데이터 세그먼트 레지스터의 시작 번지를 기억, 프로그램에서 정의된 데이터, 상수, 작업 영역의 메모리 주소 지정.
  + SS(Stack Segment Register) : 번지와 데이터를 임시로 저장할 목적으로 쓰이는 스택을 메모리에 구현, 스택 포인터 레지스터의 오프셋 값을 더하면 스택 내의 현재 워드를 가리키는 번지. 프로그램이 임시로 저장할 필요가 있거나 사용자의 피호출 서브 루팅이 사용할 데이터와 주소 포함.
  + ES(Extra Segment Register) : 지정하기 위해 본 레지스터를 사용할 때 DI 레지스터와 연관
  + FS, GS : 286이후에 추가된 레지스터로서 보조 세그먼트 레지스터
- 포인터 레지스터(Pointer Register)
  + EBP(Base Pointer) : 함수의 파라미터나 변수의 위치를 얻어오는데 간접적으로 사용(스택 메모리를 가리킴). 호출된 프로시저(Procedure)를 위한 스택 프레임 내의 고정 Reference point를 나타냄. 저장된 이전의 EBP 값을 SFP(Stack Function Flame Pointer)라고 함. SS 레지스터와 함께 사용되어 스택 내의 변수 값을 읽는 데 사용.
  + ESP(Stack Pointer) : 스택(stack)의 맨 꼭대기를 가리키는데 사용,그러나 프로그램 안에서 수시로 변경되기 때문에 특정 기준 시점을 잡아 ESP값을 EBP에 저장하여 EBP를 기준으로 변수나 패러미터에 접근. SS 레지스터와 함께 사용되며, 스택의 가장 끝 주소를 가리킴. 
  + EIP(Instaruction Pointer) : 현재 수행중인 코드를 가리킴. 다음 명령어의 오프셋(상대 위치 주소)를 저장하며 CS 레지스터와 합쳐져 다음에 수행될 명령의 주소 형성.
- 인덱스 레지스터(Index Register)
  + ESI & EDI :  메모리의 한 영역(Souce)에서 다른 영역(Destination)으로 데이터를 연속적으로
                        복사할 때 사용
- 플래그 레지스터(Flag Register) : 32비트로, 컴퓨터의 다양한 상태를 나타내는 비트 포함. 
  + ZF(Zero Flag)
  + CF(Carry Flag)



## 시스템 메모리 구조

![MemoryStructure](/Reverse/MemoryStructure.png)

- 스택(Stack)  : 후입선출(LIFO:Last-In, First Out) 방식에 의해 정보를 관리
- 힙(Heap) : 프로그램의 실행 중 필요한 기억 장소를 할당하기 위해 운영체제에 예약되어 있는 기억 장소영역. 데이터를 저장하기 위해 기억 장소를 요청하면 운영체제는 힙에 존재하는 기억 장소를 프로그램에 할당. 기억 장치가 더 이상 필요 없으면 할당 받았던 기억 장소를 운영체제에 반납, 운영체제에서는 반납된 기억 장소를 다시 힙에 돌려줌. 
- 데이터 세그먼트(Data Segment) : 초기화된 외부 변수나 Static 변수 등이 저장되는 영역
- BSS 세그먼트(Block Started Symbol Segment) : 초기화 되지 않은 전역 변수와 정정벽수가 저장되는 영역
- 텍스트 세그먼트(Text Segment) : CPU에 의해 실행되는 머신 코드가 있는 영역



## 어셈블리 문법

![AssemblyGrammar](/Reverse/AssemblyGrammar.png)

- (윈도우) Intel 문법 : Opcode (Destination) (Source)  

  `gdb> set disassembly-flavor intel`

- (리눅스) AT&T 문법 : Opcode (Source) (Destination)  

  `gdb> set disassembly-flavor att`



## 어셈블리 형식

- 연상기호/연산자(mnemonic, opcode)
- 피연산자(operand) : 레지스터, 메모리, 직접값



## 어셈블리의 기본 명령(Opcode)

- 산술 연산 명령
  + ADD(Addtion) : 덧셈 명령, 캐리를 포함하지 않는 덧셈
  + SUB(Subtraction) : 캐리를 포함하지 않는 뺄셈
  + INC(Increment) : operand 값을 1만큼 증가
  + DEC(Decrement) : operand 값을 1만큼 감소
  + CMP(Compare) : 두 데이터를 비교하여 같으면 CF(CarryFlag)는 0, ZF(Zero Flag)는 1로 설정
  + MUL(immediate Multiplication) : 부호 없는 곱셈, EAX와 operand 값을 곱셈 후 결과를 EAX에 저장
  + DIV(Dividend) : 부호 없는 나눗셈
- 데이터 전송 명령
  + MOV(Move) : 데이터 이동할 때 사용
  + LEA(Load Effective Address to register) : 데이터의 값 이동할 때 사용, MOV 명령과 LEA 명령에서 제1피연산자는 데이터 이동 공통, 제2피연산자에 대한 추가 연산의 처리 방식은 다르다.
  + PUSH(Push) : 스택에 데이터를 삽입할 때 사용
  + POP(Pop) : 스택에서 데이터를 삭제할 때 사용
- TEST(And function to flags, no result) : 데이터의 두 값을 비교할 때 사용, 데이터의 변경 없이 단순 비교
- 제어 전송 명령
  + JMP(Unconditional Jump) : 대표적인 점프 명령 프로그램을 실할 주소 또는 라벨로 이동
  + JE(Jump Equal)/JZ(Jump Zero) : (조건이 같을 경우 점프) ZF가 1일 경우 점프, 즉 비교 결과가 같을 때 점프
  + JNE(Jump not Equal)/JNZ(Jump not zero) ZF가 0일 경우 점프, 즉 비교 결과가 다를 때 점프
  + JLE(Jump less or equal) : 조건이 작거나 같을 때 점프
  + JNS(Jump not sign) : SF(Sign Flag)가 0일 때 (양수) 점프
  + CALL(Call) : JMP처럼 함수(프로지서)를 호출할 때 사용, PUSH(EIP)+JMP(jump)의 두가지 기능
  + RET(Return from Call) : 함수에서 호출한 곳으로 돌아갈 때 사용하는 명령 'POP EIP'와 같은 의미
  + INT(Interrupt) : 인터럽트가 호출되면 CS:IP(CodeSegment:InstructionPointer)와 플래그를 스택에 저장, 그 인터럽트에 관된 서브 루팅이 실행
  + LOOP(Loop CX times) : 문장들의 블록을 지정된 횟수만큼 반복, CX는 자동적으로 카운터로 사용되며, 루프가 반복할 때마다 감소



