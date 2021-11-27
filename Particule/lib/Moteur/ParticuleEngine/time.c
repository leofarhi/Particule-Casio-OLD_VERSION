static int SysCallCode[] = {0xD201422B,0x60F20000,0x80010070};
static int (*SysCall)( int R4, int R5, int R6, int R7, int FNo ) = (void*)&SysCallCode;
int getTicks()
{
    return (*SysCall)(0, 0, 0, 0, 0x3B);
}