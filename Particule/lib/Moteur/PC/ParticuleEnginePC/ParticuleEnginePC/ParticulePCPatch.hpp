#pragma once

#ifndef ClassParticuleGintPatch
#define ClassParticuleGintPatch
#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>


void Sleep(int t);
int getTicks();
bool IsKeyDown(sf::Keyboard::Key key);

#define KEY_CHAR_0 sf::Keyboard::Num0
#define KEY_CHAR_1 sf::Keyboard::Num1
#define KEY_CHAR_2 sf::Keyboard::Num2
#define KEY_CHAR_3 sf::Keyboard::Num3
#define KEY_CHAR_4 sf::Keyboard::Num4
#define KEY_CHAR_5 sf::Keyboard::Num5
#define KEY_CHAR_6 sf::Keyboard::Num6
#define KEY_CHAR_7 sf::Keyboard::Num7
#define KEY_CHAR_8 sf::Keyboard::Num8
#define KEY_CHAR_9 sf::Keyboard::Num9
#define KEY_CHAR_DP sf::Keyboard::Unknown
#define KEY_CHAR_EXP sf::Keyboard::Unknown
#define KEY_CHAR_PMINUS sf::Keyboard::Unknown
#define KEY_CHAR_PLUS sf::Keyboard::Unknown
#define KEY_CHAR_MINUS sf::Keyboard::Unknown
#define KEY_CHAR_MULT sf::Keyboard::Unknown
#define KEY_CHAR_DIV sf::Keyboard::Unknown
#define KEY_CHAR_FRAC sf::Keyboard::Unknown
#define KEY_CHAR_LPAR sf::Keyboard::Unknown
#define KEY_CHAR_RPAR sf::Keyboard::Unknown
#define KEY_CHAR_COMMA sf::Keyboard::Unknown
#define KEY_CHAR_STORE sf::Keyboard::Unknown
#define KEY_CHAR_LOG sf::Keyboard::Unknown
#define KEY_CHAR_LN sf::Keyboard::Unknown
#define KEY_CHAR_SIN sf::Keyboard::Unknown
#define KEY_CHAR_COS sf::Keyboard::Unknown
#define KEY_CHAR_TAN sf::Keyboard::Unknown
#define KEY_CHAR_SQUARE sf::Keyboard::Unknown
#define KEY_CHAR_POW sf::Keyboard::Unknown
#define KEY_CTRL_EXE sf::Keyboard::Enter
#define KEY_CTRL_DEL sf::Keyboard::Delete
#define KEY_CTRL_AC sf::Keyboard::Unknown
#define KEY_CTRL_FD sf::Keyboard::Unknown
#define KEY_CTRL_EXIT sf::Keyboard::Escape
#define KEY_CTRL_SHIFT sf::Keyboard::LShift
#define KEY_CTRL_ALPHA sf::Keyboard::LControl
#define KEY_CTRL_OPTN sf::Keyboard::RShift
#define KEY_CTRL_VARS sf::Keyboard::RControl
#define KEY_CTRL_UP sf::Keyboard::Up
#define KEY_CTRL_DOWN sf::Keyboard::Down
#define KEY_CTRL_LEFT sf::Keyboard::Left
#define KEY_CTRL_RIGHT sf::Keyboard::Right
#define KEY_CTRL_F1 sf::Keyboard::F1
#define KEY_CTRL_F2 sf::Keyboard::F2
#define KEY_CTRL_F3 sf::Keyboard::F3
#define KEY_CTRL_F4 sf::Keyboard::F4
#define KEY_CTRL_F5 sf::Keyboard::F5
#define KEY_CTRL_F6 sf::Keyboard::F6
#define KEY_CTRL_MENU sf::Keyboard::Tab

#endif