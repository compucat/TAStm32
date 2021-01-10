#include "controller_input.h"

bool initVBController(VBPort port, VBControllerType type)
{
	switch(port)
	{
		case V1_PORT:
			switch(type)
			{
				case SNES: //Clock/latch outputs, D0 input. Plus D1 input, because why not.
					;
					GPIO_InitTypeDef GPIO_InitStruct = { 0 };
					//Reconfigure visport 1 as a SNES controller reader
					//i.e. clock/latch outputs, data input
					GPIO_InitStruct.Pin = V1_CLOCK_Pin | V1_LATCH_Pin;
					GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
					HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);
					memset (&GPIO_InitStruct, 0, sizeof(GPIO_InitTypeDef));
					GPIO_InitStruct.Pin = V1_DATA_0_Pin | V1_DATA_1_Pin;
					GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
					GPIO_InitStruct.Pull = GPIO_NOPULL;
					HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);
					GPIOB->BSRR = V1_LATCH_Pin | V1_CLOCK_Pin;
					return true;
					break;
				default: return false;
			}
			break;
		default: return false;
	}
}

bool freeVBController(VBPort port) //! STUB
{
	return false;
}

VBControllerData readVBController(VBPort port)
{
	VBControllerData out;
	out.type=SNES;
	switch(port)
	{
		case V1_PORT:
			out.valid=true;
			out.snesbits=0;
			GPIOB->BSRR = V1_LATCH_Pin;
			my_wait_us_asm(5);
			GPIOB->BSRR = V1_LATCH_Pin << 16;
			my_wait_us_asm(5);
			for(int i=0; i<16; i++)
			{
				out.snesbits += ((GPIOB->IDR & V1_DATA_0_Pin) != 0) << i;
				GPIOB->BSRR = V1_CLOCK_Pin;
				my_wait_us_asm(5);
				GPIOB->BSRR = V1_CLOCK_Pin << 16;
				my_wait_us_asm(5);
			}
			break;
		default: out.valid=false;
	}
	return out;
}
