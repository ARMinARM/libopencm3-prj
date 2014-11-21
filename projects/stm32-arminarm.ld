/* Linker script for ARMinARM (STM32F103RET6, 512K flash, 64K RAM) */

/* Define memory regions. */
MEMORY
{
	rom (rx) : ORIGIN = 0x08000000, LENGTH = 512K
	ram (rwx) : ORIGIN = 0x20000000, LENGTH = 64K
}

/* Include the common ld script. */
INCLUDE libopencm3_stm32f1.ld

