#include <REGX52.H>
#include <UART.h>

#define LED P0
#define IO_A P2_4
#define IO_B P2_3
#define IO_C P2_2

int ma7doan[10] = {0x3F, 0x06, 0x5B, 0x4F, 0x66,0x6D , 0x7D, 0x07, 0x7F, 0x6F};

char a,b;
int loi;
void delay(long time){
	time = time * 25;
	while(time--){;}
	}

void Xu_Li_Led(){
	if((a == '0') && (b == '1')){
		IO_A = 0; IO_B = 0; IO_C = 0;
		LED = ma7doan[1];
		delay(1);
	}else if(a == '0' && b == '2'){
		IO_A = 0; IO_B = 0; IO_C = 0;
		LED = ma7doan[2];
		delay(1);
	}else if(a == '0' && b == '3'){
		IO_A = 0; IO_B = 0; IO_C = 0;
		LED = ma7doan[3];
		delay(1);
	}else if(a == '0' && b == '4'){
		IO_A = 0; IO_B = 0; IO_C = 0;
		LED = ma7doan[4];
		delay(1);
	}else if(a == '0' && b == '5'){
		IO_A = 0; IO_B = 0; IO_C = 0;
		LED = ma7doan[5];
		delay(1);
	}else if(a == '0' && b == '0'){
		IO_A = 0; IO_B = 0; IO_C = 0;
		LED = ma7doan[0];
		delay(1);
	}
	
}

void main()
{
	Uart_Init();
	while(1)
	{
		Uart_Write_String("Nhap Ki Tu Dieu Khien: ");
		while(Uart_Data_Ready()==0); // Doi Ki tu dieu khien
		a = Uart_Read();
		
		while(Uart_Data_Ready()==0) // Doi ki tu dieu va kiem tra loi
		{
			loi++;
			if(loi>12500) //Khoang 500ms // Co loi
			{
				Uart_Write_String("\r\n Loi Du Lieu !!!");
				break;
			}
		}
		
		if(loi<12500) // Khong co loi
		{
			b = Uart_Read();
			Uart_Write_Char(a);
			Uart_Write_Char(b);
			Xu_Li_Led();
		}
		loi = 0;
		Uart_Write_String("\r\n");
	}
}
