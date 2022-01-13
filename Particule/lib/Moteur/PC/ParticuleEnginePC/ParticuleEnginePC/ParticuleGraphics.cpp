#include "ParticuleGraphics.hpp"
#include <SFML/Graphics.hpp>
#include<iostream>

sf::RenderWindow* window;
sf::Font* font;

void ClearScreen() {
	window->clear(sf::Color::White);
};

void UpdateScreen() {
	window->display();
};

void DisplayTexture(Texture* texture, int x, int y, int Zoom = 100, int Rotate = 90) {
	if (texture->textureData != NULL) {
		sf::Sprite sprite(*texture->textureData);
		sprite.setPosition(x* ZoomScreen, y* ZoomScreen);
		sprite.setScale(ZoomScreen, ZoomScreen);
		window->draw(sprite);
	}
};

void DisplayTexture(Texture* texture, int x, int y) {
	if (texture->textureData != NULL) {
		sf::Sprite sprite(*texture->textureData);
		sprite.setPosition(x* ZoomScreen, y* ZoomScreen);
		sprite.setScale(ZoomScreen, ZoomScreen);
		window->draw(sprite);
	}
};

void DrawRectangle(int x, int y, int width, int height,sf::Color Color) {
	sf::RectangleShape rectangle(sf::Vector2f(width* ZoomScreen, height* ZoomScreen));
	rectangle.setFillColor(Color);
	rectangle.setPosition(x* ZoomScreen, y* ZoomScreen);
	window->draw(rectangle);
};

void PrintTextMini(unsigned char* text,int x,int y) {
	sf::Text uiText;
	uiText.setFont(*font);
	uiText.setCharacterSize(12* ZoomScreen);
	uiText.setFillColor(ML_BLACK);
	uiText.setString(std::string((char*)text));
	uiText.setPosition(x* ZoomScreen, y* ZoomScreen);
	window->draw(uiText);
}