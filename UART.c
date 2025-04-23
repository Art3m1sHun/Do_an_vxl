#include <REGX51.H>
#include <UART.h>

void Uart_Init()
{
	// Khoi tao UART o mode 1, 9600 baud
	SM0 = 0; SM1 = 1;		// Chon UART mode 1
	TMOD = 0x20;            // 0010 xxxx - Timer1 hoat dong o che do 8bit tu dong nap lai
	TH1 = 0xFD;				// Toc do baud 9600
	TR1 = 1;				// Timer1 bat dau chay
	TI = 1;					// San sang gui du lieu
	REN = 1;				// Cho phep nhan du lieu
}

void Uart_Write_Char(char c)
{
 	while(TI == 0);
	TI = 0;
	SBUF = c;
}

void Uart_Write_String(char * str)
{
	unsigned char i = 0;
 	while(str[i]!=0)
	{
		Uart_Write_Char(str[i]);
		i++;
	}
}

char Uart_Data_Ready()
{
	return RI;
}

char Uart_Read()
{
	RI = 0;
	return SBUF;
}
