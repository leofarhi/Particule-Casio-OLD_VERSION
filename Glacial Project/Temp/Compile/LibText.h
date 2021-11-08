#ifndef _LIBTEXT_H
#define _LIBTEXT_H

#define TXT_FONTS 10

void Txt_Init  (int);
void Txt_Pixel (int,int,int);
void Txt_Point (int,int,int,int);
int  Txt_Get   (int,int);
void Txt_Text  (const char *,int,int,int,int);
void Txt_Quit  (void);

void Txt_Char(char c, int x, int y, int f, int w, int h, int m,int startY,int endY);
void Txt_text_taille(const char *s, int x, int y, int f, int m,int startY,int endY);

#define TXT_OR  0x01
#define TXT_ON  0x02
#define TXT_AND 0x04
#define TXT_REV 0x08
#define TXT_XOR 0x10

#define TXT_MINISD          0x00
#define TXT_7SEGMINI        0x01
#define TXT_SYSTEM          0x02
#define TXT_7SEG            0x03
#define TXT_ARCADIUM        0x04
#define TXT_SERIF           0x05
#define TXT_SERIFITALIC     0x06
#define TXT_SERIFBOLD       0x07
#define TXT_SERIFBOLDITALIC 0x08
#define TXT_RUNES           0x09

#define FONT_MINISD          0x0001
#define FONT_7SEGMINI        0x0002
#define FONT_SYSTEM          0x0004
#define FONT_7SEG            0x0008
#define FONT_ARCADIUM        0x0010
#define FONT_SERIF           0x0020
#define FONT_SERIFITALIC     0x0040
#define FONT_SERIFBOLD       0x0080
#define FONT_SERIFBOLDITALIC 0x0100
#define FONT_RUNES           0x0200
#define FONT_ALL             0xFFFF

#endif // _LIBTEXT_H
