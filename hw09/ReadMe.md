# hw09 grading

| Points      | Description |
| ----------- | ----------- |
|  5 | Project Timeline
| 10 | Logging to Sheets
|  3 | Logging to ThingSpeak - optional
|  2 | Extras
| 20 | **Total**

*My comments are in italics. --may*

# Homework 9: Project  
BBIO Project information will be updated on wiki.  
BBIO file is mostly finished with the exception of event detection.  
All other files are finished.  
Project is being developed for kernel 4.19 only.  
Event detection will be finished by Tuesday November 10th.  
Final paper and presentation will be finished by the day before the Final time.  

*Could you try it on the 5.4 or 5.8 kernel just to see how it works?*

# Homework 9: Google Sheets  
tmp101.py is the program that reads temperatures and updates it on a google sheet.  
The website for google sheet is https://docs.google.com/spreadsheets/d/1kctAdOg2-cbQTDXBYDEIKHwuDa5a3wODE2u6K-a3CU8/edit#gid=0  
The google sheet displays the date time, temp in Celsius, and temp in Fahrenheit in 3 columns.  
I ran the code for 1000 times, and it gave an error after inputting the 154th line into the google sheet.  
Quota reached limit "Write requests per user per 100 seconds of service"  
The api can only handle so many lines of editing on a single google sheet per second.  

*Yup, there are some limits for the free tier.*

### Installation instructions  
credential.json and tmp101.py are already set up to use the google sheet on the website above.  
tmp101 takes one additional command line argument that is the number of times you want the program to update the temperature on the google sheet.  
./tmp101.py 100    
# Homework 9: Think Speak  
temp.py is a program that logs temperature from a tmp101 sensor to ThingSpeak.  
The channel is 1214678. Url = https://thingspeak.com/channels/1214678/private_show  
It only logs temperature once every 15 minutes.  
The program only uses one temp101 sensor, so Field 2 readings are always set to 0.  
![screenshot of thingspeak](https://github.com/EricMorse/ECE434/tree/master/hw09/screenshot.png)  
### Installation instructions
Run setup.sh to export thingspeak credentials.  
The program uses no command link arguments, so ./tmp101.py will run the program.  


