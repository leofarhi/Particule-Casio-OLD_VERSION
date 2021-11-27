#pragma once

#ifndef ClassParticuleGintPatch
#define ClassParticuleGintPatch

#include <gint/rtc.h>
#include <gint/keyboard.h>
#include <gint/timer.h>
#include <gint/clock.h>
void Sleep(int t);
int getTicks();
bool IsKeyDown(int key);

#define KEY_CHAR_0 KEY_0
#define KEY_CHAR_1 KEY_1
#define KEY_CHAR_2 KEY_2
#define KEY_CHAR_3 KEY_3
#define KEY_CHAR_4 KEY_4
#define KEY_CHAR_5 KEY_5
#define KEY_CHAR_6 KEY_6
#define KEY_CHAR_7 KEY_7
#define KEY_CHAR_8 KEY_8
#define KEY_CHAR_9 KEY_9
#define KEY_CHAR_DP KEY_DP
#define KEY_CHAR_EXP KEY_EXP
#define KEY_CHAR_PMINUS KEY_PMINUS
#define KEY_CHAR_PLUS KEY_PLUS
#define KEY_CHAR_MINUS KEY_MINUS
#define KEY_CHAR_MULT KEY_MULT
#define KEY_CHAR_DIV KEY_DIV
#define KEY_CHAR_FRAC KEY_FRAC
#define KEY_CHAR_LPAR KEY_LPAR
#define KEY_CHAR_RPAR KEY_RPAR
#define KEY_CHAR_COMMA KEY_COMMA
#define KEY_CHAR_STORE KEY_STORE
#define KEY_CHAR_LOG KEY_LOG
#define KEY_CHAR_LN KEY_LN
#define KEY_CHAR_SIN KEY_SIN
#define KEY_CHAR_COS KEY_COS
#define KEY_CHAR_TAN KEY_TAN
#define KEY_CHAR_SQUARE KEY_SQUARE
#define KEY_CHAR_POW KEY_POW
#define KEY_CTRL_EXE KEY_EXE
#define KEY_CTRL_DEL KEY_DEL
#define KEY_CTRL_AC KEY_AC
#define KEY_CTRL_FD KEY_FD
#define KEY_CTRL_EXIT KEY_EXIT
#define KEY_CTRL_SHIFT KEY_SHIFT
#define KEY_CTRL_ALPHA KEY_ALPHA
#define KEY_CTRL_OPTN KEY_OPTN
#define KEY_CTRL_VARS KEY_VARS
#define KEY_CTRL_UP KEY_UP
#define KEY_CTRL_DOWN KEY_DOWN
#define KEY_CTRL_LEFT KEY_LEFT
#define KEY_CTRL_RIGHT KEY_RIGHT
#define KEY_CTRL_F1 KEY_F1
#define KEY_CTRL_F2 KEY_F2
#define KEY_CTRL_F3 KEY_F3
#define KEY_CTRL_F4 KEY_F4
#define KEY_CTRL_F5 KEY_F5
#define KEY_CTRL_F6 KEY_F6
#define KEY_CTRL_MENU KEY_MENU

#endif