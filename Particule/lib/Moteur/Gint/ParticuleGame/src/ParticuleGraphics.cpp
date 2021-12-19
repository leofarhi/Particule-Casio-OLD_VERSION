#include "ParticuleGraphics.hpp"
#include <gint/display.h>
#include "ParticuleGintPatch.hpp"


void ClearScreen() {
	dclear(C_WHITE);
};

void UpdateScreen() {
	dupdate();
};

void DisplayTexture(Texture* texture, int x, int y, int Zoom = 100, int Rotate = 90) {
	if (texture->textureData!=NULL)
		dimage(x, y, texture->textureData);
};

void DisplayTexture(Texture* texture, int x, int y) {
	if (texture->textureData != NULL)
		dimage(x, y, texture->textureData);
};

void DrawRectangle(int x, int y, int width, int height,int Color) {
	drect(x, y, x + width, y + height, Color);
};

void PrintTextMini(unsigned char* text,int x,int y) {
	dtext(x, y, C_BLACK, (const char*)text);
}