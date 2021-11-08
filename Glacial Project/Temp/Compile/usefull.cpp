#include "usefull.h"
extern "C"
{
#include "keybios.h"
#include "fxlib.h"
#include <stdio.h>
#include "stdio.h"
#include "stdlib.h"

#include "string.h"
#include "time.h"
#include "MonochromeLib.h"
#define SCA 0xD201D002
#define SCB 0x422B0009
#define SCE 0x80010070

	/************************************

	Classe d'utilitaires divers

	************************************/

	typedef int(*sc_i2cp2sip) (char*, char*, short int*, short int*);
	typedef int(*sc_iv) (void);
	typedef int(*sc_4i) (int, int, int);

	const unsigned int sc003b[] = { SCA, SCB, SCE, 0x3B };
	const unsigned int sc0015[] = { SCA, SCB, SCE, 0x0015 };
	const unsigned int sc0248[] = { SCA, SCB, SCE, 0x248 };

#define RTC_GetTicks (*(sc_iv)sc003b)
#define PutKey (*(sc_4i)sc0248)
#define GlibGetOSVersionInfo (*(sc_i2cp2sip)sc0015)

	int OSVersionAsInt(void)
	{
		char mainversion;
		char minorversion;
		short release;
		short build;
		/*unsigned char mainversion;
		unsigned char minorversion;
		unsigned short release;
		unsigned short build;*/
		GlibGetOSVersionInfo(&mainversion, &minorversion, &release, &build);
		return ((mainversion << 24) & 0xFF000000) | ((minorversion << 16) & 0x00FF0000) | (release & 0x0000FFFF);
	}
#define isOS2 (OSVersionAsInt() >= 0x02020000)
#define OS2(x,y) ((OSVersionAsInt() >= 0x02020000)?y:x)
    unsigned char GetKeyMod(unsigned int* key)
    {
        unsigned char x, ret;

        ret = GetKey(key);

        for (x = 0; x < 80; x++)
        {
            if (KeyDown(x))
            {
                *key = x;
                break;
            }
        }
        return ret;
    }
    void delay(void)
    {
        char i;
        for (i = 0; i < 5; i++) {};
    }
    unsigned char CheckKeyRow(unsigned char code)
    {
        unsigned char result = 0;
        short* PORTB_CTRL = (short*)0xA4000102;
        short* PORTM_CTRL = (short*)0xA4000118;
        char* PORTB = (char*)0xA4000122;
        char* PORTM = (char*)0xA4000138;
        char* PORTA = (char*)0xA4000120;
        /*short*PORTB_CTRL=(void*)0xA4000102;
        short*PORTM_CTRL=(void*)0xA4000118;
        char*PORTB=(void*)0xA4000122;
        char*PORTM=(void*)0xA4000138;
        char*PORTA=(void*)0xA4000120;*/
        short smask;
        char cmask;
        unsigned char column, row;
        column = code >> 4;
        row = code & 0x0F;
        smask = 0x0003 << ((row % 8) * 2);
        cmask = ~(1 << (row % 8));
        if (row < 8)
        {
            *PORTB_CTRL = 0xAAAA ^ smask;
            *PORTM_CTRL = (*PORTM_CTRL & 0xFF00) | 0x00AA;
            delay();
            *PORTB = cmask;
            *PORTM = (*PORTM & 0xF0) | 0x0F;
        }
        else
        {
            *PORTB_CTRL = 0xAAAA;
            *PORTM_CTRL = ((*PORTM_CTRL & 0xFF00) | 0x00AA) ^ smask;
            delay();
            *PORTB = 0xFF;
            *PORTM = (*PORTM & 0xF0) | cmask;
        }

        delay();
        result = (~(*PORTA)) >> column & 1;
        delay();
        *PORTB_CTRL = 0xAAAA;
        *PORTM_CTRL = (*PORTM_CTRL & 0xFF00) | 0x00AA;
        delay();
        *PORTB_CTRL = 0x5555;
        *PORTM_CTRL = (*PORTM_CTRL & 0xFF00) | 0x0055;
        delay();

        return result;
    }

    unsigned char KeyDown(unsigned char keycode)
    {
        unsigned short key[8];
        const unsigned short* keyboardregister = (unsigned short*)0xA44B0000;
        if (isOS2)
        {
            unsigned char row = keycode % 10;
            memcpy(key, keyboardregister, sizeof(unsigned short) << 3);

            return (0 != (key[row >> 1] & 1 << keycode / 10 - 1 + ((row & 1) << 3)));
        }
        else
        {
            return CheckKeyRow((keycode % 10) + ((keycode / 10 - 1) << 4));
        }
    }


}