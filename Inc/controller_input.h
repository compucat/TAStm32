#pragma once
/**
@file controller_input.h
@brief Contains methods to use the visboard ports as controller inputs (with appropriate adapters).

Currently supported: SNES controllers can be read from port 1.

Not yet implemented:
- Visboard port arbitration/failsafe (requires extracting visboard code from TASRun code)
- NES/N64/GCN controller support
- Visboard port 2 support
*/

#include "stm32f4xx_hal.h"
#include "main.h"
#include <string.h> //memset?
#include <stdint.h>
#include <stdbool.h>
void my_wait_us_asm(int n);

typedef enum {V1_PORT, V2_PORT} VBPort;
typedef enum {NES, SNES, N64, GCN} VBControllerType;
typedef struct
{
	bool valid; //!< If this is false, then the controller data is invalid (for example, if reading from an uninitialized port).
	VBControllerType type; //!< The type of controller.
	uint16_t snesbits; //!< TEMPORARY HACK: Raw SNES controller bits.
} VBControllerData;

/**
Initializes the selected visboard port to read a controller of the selected type.

@return Returns true if successful and false otherwise (for example, if the visboard ports are already in use).
@param port The visboard port to use.
@param type The type of controller to expect.
*/
bool initVBController(VBPort port, VBControllerType type);

/**
Deinitializes the selected visboard port, freeing it to be otherwise used.

@return Returns true if successful. Returns false if the port is claimed by something else.
@param port The visboard port to free.
*/
bool freeVBController(VBPort port);

/**
Reads controller data from the selected port.

@return Returns the read controller data.
@param port The port to read from.
*/
VBControllerData readVBController(VBPort port);
