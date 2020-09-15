// Blink pin 60 at 1 Hz
//
//Created by Dingo_aus, 7 January 2009
//email: dingo_aus [at] internode <dot> on /dot/ net
// From http://www.avrfreaks.net/wiki/index.php/Documentation:Linux/GPIO#gpio_framework
//
//Created in AVR32 Studio (version 2.0.2) running on Ubuntu 8.04
// Modified by Mark A. Yoder, 21-July-2011
// Modified by Mark A. Yoder 30-May-2013

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <signal.h>
#include "gpio-utils.h"

/******************************************
 * Global variables
 ****************************************/
int keepgoing = 1;   // Set to 0 when crl-c is pressed

/****************************************
 * signal_handler
 ****************************************/
void signal_handler(int sig);
// Callback called whe SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
     printf("Ctrl-C pressed, cleanin up and exiting..\n");
     keepgoing = 0;
}

/********************************************
 * Main
 ********************************************/

int main(int argc, char** argv)
{
	//create a variable to store whether we are sending a '1' or a '0'
	char set_value[5]; 
	//Integer to keep track of whether we want on or off
	int toggle = 0;
	int onTime;	// Time in micro sec to keep the signal on
        int offTime;    // Time in micro sec to keep the signal off
	int gpio = 60;
	int gpio_fd;

	if (argc < 4) {
		printf("Usage: %s <on/off time in us>\n\n", argv[0]);
		printf("Toggle gpio 60 at the period given\n");
                printf("Port is selectong on argv[3]\n");
		exit(-1);
	}
	onTime = atoi(argv[1]);
        offTime = atoi(argv[2]);
        if(argv[3]){
          gpio = atoi(argv[3]);
        } else {
          printf("Didn't get port number argument.  Using 60 instead\n");
          gpio = 60;
        }
        
        // Set the signal callback for Ctrl-C
        signal(SIGINT, signal_handler);

	printf("**********************************\n"
		"*  Welcome to PIN Blink program  *\n"
		"*  ....blinking gpio 60          *\n"
		"*  ....period of %d us.........*\n"
		"**********************************\n", 2*(onTime+offTime));

	//Using sysfs we need to write the gpio number to /sys/class/gpio/export
	//This will create the folder /sys/class/gpio/gpio60
	gpio_export(gpio);

	printf("...export file accessed, new pin now accessible\n");
	
	//SET DIRECTION
	gpio_set_dir(gpio, "out");
	printf("...direction set to output\n");
			
	gpio_fd = gpio_fd_open(gpio, O_RDONLY);
        //lseek line version commented out
        //gpio_fd = lseek(gpio, onOffTime, 0);
	
        //Run an infinite loop - will require Ctrl-C to exit this program
	while(keepgoing)
	{
		toggle = !toggle;
		gpio_set_value(gpio, toggle);
//		printf("...value set to %d...\n", toggle);

		//Pause for a while
                if(toggle){
                  usleep(onTime);
                } else {
                  usleep(offTime);
                }
	}
	gpio_fd_close(gpio_fd);
	return 0;
}
