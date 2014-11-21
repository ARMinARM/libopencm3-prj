#ifndef _USBHIDMOUSE_H_
#define _USBHIDMOUSE_H_

// 9 buttons connected to A0-A8
#define BUTTON0	   (1 << 0) // left btn
#define BUTTON1	   (1 << 1) // right btn
#define BUTTON2	   (1 << 2) // middle btn
#define BUTTON3	   (1 << 3) // - rel x
#define BUTTON4	   (1 << 4) // + rel x
#define BUTTON5	   (1 << 5) // - rel y
#define BUTTON6	   (1 << 6) // + rel y
#define BUTTON7	   (1 << 7) // - rel wheel
#define BUTTON8	   (1 << 8) // + rel wheel

#define BUTTON_MASK  (BUTTON0 | BUTTON1 | BUTTON2 | BUTTON3 | BUTTON4 | BUTTON5 | BUTTON6 | BUTTON7 | BUTTON8)

void button_setup(void);
uint16_t buttons_get_status(void);
void check_and_send(usbd_device *usbd_dev);

#endif /* USBHIDMOUSE_H */ 
