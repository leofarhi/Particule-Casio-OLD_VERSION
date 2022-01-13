#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>

int getTicks() {
	return 0;
}

bool IsKeyDown(sf::Keyboard::Key key) {
	return sf::Keyboard::isKeyPressed(key);
}

void Sleep(int t) {
	//sleep(t);
}