#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>
#include <iostream>
#include "ParticuleGraphics.hpp"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

///////
#include "Announcement.h"
#include "List.h"
#include "ParticuleEngine.hpp"
#include "ParticuleGraphics.hpp"
#include "Ressources.h"
///////


int main()
{	
	static SceneManager* sceneManager = new SceneManager();

	window = new sf::RenderWindow(sf::VideoMode(
		sceneManager->projectSettings->ScreenSize->x* ZoomScreen,
		sceneManager->projectSettings->ScreenSize->y* ZoomScreen),
		"ParticuleEngine");
	font = new sf::Font();
	font->loadFromFile("Fonts/KenneyFuture.ttf");

	//AddImages
	//CreateTextures
	//reference croise
	sceneManager->LoadScene(0);
	sceneManager->StartScene();

	sf::Event event;

	while (window->isOpen()) {

		while (window->pollEvent(event)) {

			if (event.type == sf::Event::Closed) {

				window->close();
			}
		}

		ClearScreen();
		sceneManager->UpdateScene();

		//Sleep(100);///////////////////////////////////////
		UpdateScreen();
	}
	delete sceneManager;

	return 0;
}