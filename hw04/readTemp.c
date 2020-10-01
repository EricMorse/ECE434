#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <signal.h>

#define BUFFER_SIZE 50

/***************************************
* Global variables
***************************************/
static volatile int keepgoing = 1;  // set to 0 when ctrl-c is pressed
/**************************************
* signal handler
**************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent
void signal_handler(int sig)
{
	printf("\nCtrl-C pressed, cleaning up and exiting...\n");
	keepgoing = 0;
}


int main(int argc, char *argv[]) {
  //int temp_file;
  FILE *temp_file;
  char buffer[BUFFER_SIZE];
  int read_size;
  int temp;
  double temp2;
  // attempts to create tmp101 automatically
  // only works when program is run as root
  system("cd /sys/class/i2c-adapter/i2c-2");
  system("echo tmp101 0x48 > new device");
  signal(SIGINT, signal_handler);
  
  while(keepgoing)
  {
    /***************************************************
    * opens file and checks if temp1_input exists.
    * if it does not exist, follow instructions in ReadMe.md
    ****************************************************/
    temp_file = fopen("/sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0/temp1_input", "r");
    if(temp_file == NULL)
    {
      printf("Error: temp1_input file not found\n");
      printf("Program must be run under root\n");
      printf("or type below into command prompt\n");
      printf("cd /sys/class/i2c-adapter/i2c-c\n");
      printf("sudo echo tmp101 0x48 > new device\n");
      return(-1);
    }
    //reads temperature and converts it to Fahrenheit
    fscanf(temp_file, "%d", &temp);
    temp2 = (((float)temp)/1000.0*9.0/5.0)+32;
    printf("Temperature = %f F\n", temp2);
    fclose(temp_file);
    usleep(300000);    // long usleep to prevent screen from being spammed
  }
  
  return 0;
}
