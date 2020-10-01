/*****************************************
* Created by Eric Morse
* Toggles gpio pin as quickly as possible
* Uses command line arguments for toggle time
* Sets pin P9_14, aka GPIO_50, as toggle pin
*****************************************/
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <unistd.h>
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
static volatile int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
   volatile void *gpio_addr;
   volatile unsigned int *gpio_oe_addr;
   volatile unsigned int *gpio_setdataout_addr;
   volatile unsigned int *gpio_cleardataout_addr;
   unsigned int reg;
  
   int onOffTime;

   if (argc < 2){
       printf("Usage: %s <on/off time in us>\n\n", argv[0]);
       printf("toggles GPIO_50 or pin P9_14\n\n");
       exit(-1);
    }
    onOffTime = atoi(argv[1]);
    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;
    // if mapping fails, check config-pin section of program in ReadMe.md
    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio_addr);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr);

    // Set GPIO_50 to be an output pin
    reg = *gpio_oe_addr;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~(GPIO_50);       // Set GPIO_50 bit to 0
    *gpio_oe_addr = reg;
    printf("GPIO1 configuration: %X\n", reg);

    printf("Started toggling GPIO_50\n");
    //usleep commented out for speed testing without usleep
    while(keepgoing) {
        *gpio_setdataout_addr = GPIO_50;
        usleep(onOffTime);
        *gpio_cleardataout_addr = GPIO_50;
        usleep(onOffTime);
    }

    munmap((void *)gpio_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
