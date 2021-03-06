/*
 * usbplayback.h
 *
 *  Created on: 9 Sep 2020
 *      Author: user
 */

#ifndef USBPLAYBACK_USBPLAYBACK_H_
#define USBPLAYBACK_USBPLAYBACK_H_

#include "TASRun.h"

typedef enum
{
	RUNSTATE_STOPPED,
	RUNSTATE_RUNNING,
	RUNSTATE_FINISHING, // File has ended and we're just waiting for the buffer to run out
	RUNSTATE_STOPPING, // Playback is finished and state should reset
} PlaybackState;

extern PlaybackState USBPlaybackState;

uint8_t USB_Playback_Init();
void USB_Playback_Task();
void USB_Start_Tas(char *file);
void USB_Stop_TAS();
void USB_Playback_Task();
int load_tcf(char *filename);

#endif /* USBPLAYBACK_USBPLAYBACK_H_ */
