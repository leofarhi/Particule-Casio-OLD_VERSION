extern "C"
{
#pragma once
#ifndef USEFULL_H
#define USEFULL_H

#define OS2(x,y) ((OSVersionAsInt() >= 0x02020000)?y:x)
	/*
	void key_inject(int keycode);
	void key_inject1(int keycode);
	unsigned char key_down(unsigned char code); // fonction plus rapide et compatible SH4 de IsKeyDown()
	int time_getTicks(); //renvoye le nombre de ticks (1/128 de seconde) depuis minuit selon le processeur de la calto
	int getFps(); //renvoye le nombre de FPS
	void setFps(int fpsWish); //regle le nombre de fps : 1 pour 128 FPS,2 pour 64, 4 pour 32, 5 pour 25 => 128/fpsWish
	int max(int a,int b);  //renvoye le max
	int min(int a,int b);
	int random(int max);
	int abs(int nombre);
	int writeFile(unsigned char* name,unsigned char* extension,unsigned char* source,int taille);*/
	/*
	fonction de sauvegarde
	ecrit taille octets du tableau source dans le fichier name.extension
	Pour ecrire un tableau d'int, castez simplement le tableau (unsigned char*)tableauDInt
	Pour ecrire un int simple, faites writeFile(name,extension,(unsigned char*)&variable,4);
	*/
	//int readFile(unsigned char* name,unsigned char* extension,unsigned char* reception);
	/*
	fonction de chargement de sauvegarde
	ecrit le contenu du fichier name.extension dans le tableau reception
	pour lui passer un tableau d'int, castez simplement le tableau (unsigned char*)tableauDInt
	Pour ecrire dans un int simple, faites writeFile(name,extension,(unsigned char*)&variable); mais faites attention a ce que le fichier ne soit pas >4 octets
	*/

	void delay(void);
	unsigned char CheckKeyRow(unsigned char code);
	unsigned char KeyDown(unsigned char keycode);
	unsigned char GetKeyMod(unsigned int* key);


#define __KEYBIOS_H__
#include "fxlib.h"
#define KEY_CHAR_0 71
#define KEY_CHAR_1 72
#define KEY_CHAR_2 62
#define KEY_CHAR_3 52
#define KEY_CHAR_4 73
#define KEY_CHAR_5 63
#define KEY_CHAR_6 53
#define KEY_CHAR_7 74
#define KEY_CHAR_8 64
#define KEY_CHAR_9 54
#define KEY_CHAR_DP 61
#define KEY_CHAR_EXP 51
#define KEY_CHAR_PMINUS 41
#define KEY_CHAR_PLUS 42
#define KEY_CHAR_MINUS 32
#define KEY_CHAR_MULT 43
#define KEY_CHAR_DIV 33
#define KEY_CHAR_FRAC 75
#define KEY_CHAR_LPAR 55
#define KEY_CHAR_RPAR 45
#define KEY_CHAR_COMMA 35
#define KEY_CHAR_STORE 25
#define KEY_CHAR_LOG 66
#define KEY_CHAR_LN 56
#define KEY_CHAR_SIN 46
#define KEY_CHAR_COS 36
#define KEY_CHAR_TAN 26
#define KEY_CHAR_SQUARE 67
#define KEY_CHAR_POW 57
#define KEY_CTRL_EXE 31
#define KEY_CTRL_DEL 44
#define KEY_CTRL_AC 32
#define KEY_CTRL_FD 65
#define KEY_CTRL_EXIT 47
#define KEY_CTRL_SHIFT 78
#define KEY_CTRL_ALPHA 77
#define KEY_CTRL_OPTN 68
#define KEY_CTRL_VARS 58
#define KEY_CTRL_UP 28
#define KEY_CTRL_DOWN 37
#define KEY_CTRL_LEFT 38
#define KEY_CTRL_RIGHT 27
#define KEY_CTRL_F1 79
#define KEY_CTRL_F2 69
#define KEY_CTRL_F3 59
#define KEY_CTRL_F4 49
#define KEY_CTRL_F5 39
#define KEY_CTRL_F6 29
#define KEY_CTRL_MENU 48

#define isOS2 (OSVersionAsInt() >= 0x02020000)
#define OS2(x,y) ((OSVersionAsInt() >= 0x02020000)?y:x)

#define IsKeyDown(x) KeyDown(x)
#define IsKeyUp(x) !KeyDown(x)
//#define GetKey(x) GetKeyMod(x)
#endif
}