#include "ParticuleGintPatch.hpp"
#include <gint/display.h>
#include <gint/rtc.h>
#include <gint/keyboard.h>
#include <gint/timer.h>
#include <gint/clock.h>
int getTicks() {
	return rtc_ticks();
}

bool IsKeyDown(int key) {
	return keydown(key);
}

void Sleep(int t) {
	sleep(t);
}