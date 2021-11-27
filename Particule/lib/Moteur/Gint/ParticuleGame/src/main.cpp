#include <gint/display.h>
#include <gint/keyboard.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//////////////////
#include "Announcement.h"
#include "List.h"
#include "ParticuleEngine.hpp"
#include "ParticuleGraphics.hpp"
#include <gint/keyboard.h>
#include "Ressources.h"
/////////////////

int main(void)
{
    extern font_t font;
    dfont(&font);

    static SceneManager* sceneManager = new SceneManager();
    //AddImages
    //CreateTextures
    //reference croise
    sceneManager->LoadScene(0);
    sceneManager->StartScene();
    while (!IsKeyDown(KEY_CTRL_MENU) && (!sceneManager->_quit))
    {
        ClearScreen();
        clearevents();
        sceneManager->UpdateScene();

        //Sleep(100);///////////////////////////////////////
        UpdateScreen();
    }
    delete sceneManager;
    return 1;
}