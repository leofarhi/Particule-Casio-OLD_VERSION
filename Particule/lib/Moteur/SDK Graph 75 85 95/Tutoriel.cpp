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
#include "ClassParticule.h"
//#include "string.h"
#include "MonochromeLib.h"
#include "Images.h"


int main() {
    int SceneInBuild[] = {0};

    SceneManager scene(SceneInBuild);

    ML_display_vram();

    //Bdisp_AllClr_DDVRAM();


    /*locate(1, 4);
    Print((unsigned char*)"This application is");
    locate(1, 5);
    Print((unsigned char*)" sample Add-In.");
    locate(1, 6);
    Print((unsigned char*)" create by Farhi");*/


    while (1) {
        ML_clear_vram();
        for (int i(0); i < scene.AllElemLength; ++i)
        {
            if (scene.AllElem[i]->x - scene.CamX + scene.AllElem[i]->w > 0 && scene.AllElem[i]->x - scene.CamX < 128 && scene.AllElem[i]->y - scene.CamY + scene.AllElem[i]->h>0 && scene.AllElem[i]->y - scene.CamY < 64) {
                for (int j(0); j < scene.AllElem[i]->AllCompoLength; ++j)
                {
                    scene.AllElem[i]->AllCompo[j]->OnUpdate();
                }
                scene.AllElem[i]->afficher(scene.CamX, scene.CamY);
            }
        }

        Sleep(100);
        ML_display_vram();
    }

    return 1;
}

extern "C"
{
int AddIn_main(int isAppli, unsigned short OptionNum)
{
    return main();
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
