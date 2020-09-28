// sets two pins GPIO_50 and GPIO_51 to be read as button pins
// when each button is pressed, corresponding USR LED lights up
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
    volatile void *gpio_addr1;
    volatile void *gpio_addr2;
    volatile unsigned int *gpio_oe_addr1;
    volatile unsigned int *gpio_oe_addr2;
    volatile unsigned int *gpio_datain1;
    volatile unsigned int *gpio_datain2;
    volatile unsigned int *gpio_setdataout_addr1;
    volatile unsigned int *gpio_setdataout_addr2;
    volatile unsigned int *gpio_cleardataout_addr1;
    volatile unsigned int *gpio_cleardataout_addr2;
    unsigned int reg1;
    unsigned int reg2;
    
    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio_addr1 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio_addr2 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio_oe_addr1          = gpio_addr1 + GPIO_OE;
    gpio_oe_addr2          = gpio_addr2 + GPIO_OE;
    gpio_datain1           = gpio_addr1 + GPIO_DATAIN;
    gpio_datain2           = gpio_addr2 + GPIO_DATAIN;
    gpio_setdataout_addr1  = gpio_addr1 + GPIO_SETDATAOUT;
    gpio_setdataout_addr2  = gpio_addr2 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr1 = gpio_addr1 + GPIO_CLEARDATAOUT;
    gpio_cleardataout_addr2 = gpio_addr2 + GPIO_CLEARDATAOUT;

    if(gpio_addr1 == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    if(gpio_addr2 == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }

    // Set USR3 to be an output pin
    reg1 = *gpio_oe_addr1;
    reg1 &= ~(USR3);       // Set USR3 bit to 0
    *gpio_oe_addr1 = reg1;
    // Set USR1 to be an output pin
    reg2 = *gpio_oe_addr2;
    reg2 &= ~(USR1);

    printf("Ready for button input\n");
    while(keepgoing) {
        if(*gpio_datain1 & GPIO_50) {
          *gpio_setdataout_addr1 = USR3;
        } else {
           *gpio_cleardataout_addr1 = USR3;
        }
        if(*gpio_datain2 & GPIO_51) {
          *gpio_setdataout_addr2 = USR1;
        } else {
          *gpio_cleardataout_addr2 = USR1;
        }
    }

    munmap((void *)gpio_addr1, GPIO1_SIZE);
    munmap((void *)gpio_addr2, GPIO1_SIZE);
    close(fd);
    return 0;
}
