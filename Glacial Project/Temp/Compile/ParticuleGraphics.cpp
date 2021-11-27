#include "ParticuleGraphics.hpp"
#include "MonochromeLib.h"
#include "usefull.h"

void ClearScreen() {
	ML_clear_vram();
};

void UpdateScreen() {
	ML_display_vram();
};

void DisplayTexture(Texture* texture, int x, int y, int Zoom = 100, int Rotate = 90) {
	ML_bmp_or_cl((const unsigned char*)texture->textureData, x, y, texture->width, texture->height);
};

void DisplayTexture(Texture* texture, int x, int y) {
	ML_bmp_or_cl((const unsigned char*)texture->textureData, x, y, texture->width, texture->height);
};

void DrawRectangle(int x, int y, int width, int height, ML_Color Color) {
	ML_rectangle(x, y, x + width, y + height, 0, Color, Color);
};

void PrintTextMini(unsigned char* text,int x,int y) {
	PrintMini(x, y, (unsigned char*)text, MINI_OVER);
}