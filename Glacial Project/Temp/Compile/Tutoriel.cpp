/*****************************************************************/
/*                                                               */
/*   CASIO fx-9860G SDK Library                                  */
/*                                                               */
/*   File name : [ProjectName].c                                 */
/*                                                               */
/*   Copyright (c) 2006 CASIO COMPUTER CO., LTD.                 */
/*                                                               */
/*****************************************************************/

extern "C"
{
#include "keybios.h"
#include "fxlib.h"
#include <stdio.h>
#include "stdio.h"
#include "stdlib.h"

#include "string.h"
#include "time.h"




}
#include "usefull.h"

//****************************************************************************
//  AddIn_main (Sample program main function)
//
//  param   :   isAppli   : 1 = This application is launched by MAIN MENU.
//                        : 0 = This application is launched by a strip in eACT application.
//
//              OptionNum : Strip number (0~3)
//                         (This parameter is only used when isAppli parameter is 0.)
//
//  retval  :   1 = No error / 0 = Error
//
//****************************************************************************
#include "Announcement.h"
#include "List.h"
#include "ParticuleEngine.hpp"
//#include "ClassParticule.h"
//#include "string.h"
#include "MonochromeLib.h"
#include "Ressources.h"



int main() {
    static SceneManager* sceneManager = new SceneManager();
    //reference croise
    sceneManager->LoadScene(0);
    sceneManager->StartScene();
    while (!IsKeyDown(KEY_CTRL_MENU) && (!sceneManager->_quit))
    {
        ML_clear_vram();
        sceneManager->UpdateScene();

        Sleep(100);
        ML_display_vram();
    }
    delete sceneManager;
    return 1;
}

extern "C"
{
int AddIn_main(int isAppli, unsigned short OptionNum)
{
    main();
    unsigned int key;
    return GetKey(&key);
}




//****************************************************************************
//**************                                              ****************
//**************                 Notice!                      ****************
//**************                                              ****************
//**************  Please do not change the following source.  ****************
//**************                                              ****************
//****************************************************************************


#pragma section _BR_Size
unsigned long BR_Size;
#pragma section


#pragma section _TOP

//****************************************************************************
//  InitializeSystem
//
//  param   :   isAppli   : 1 = Application / 0 = eActivity
//              OptionNum : Option Number (only eActivity)
//
//  retval  :   1 = No error / 0 = Error
//
//****************************************************************************
int InitializeSystem(int isAppli, unsigned short OptionNum)
{
    return INIT_ADDIN_APPLICATION(isAppli, OptionNum);
}

#pragma section
}
